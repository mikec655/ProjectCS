#include <stdint.h>
#include "const.h"
#include "scheduler.h"
#include "distance.h"
#include <avr/interrupt.h>
#include <avr/io.h>
#include <util/delay.h>


// Uitrolwaardes
int8_t MAX_UITROL;
int8_t MIN_UITROL;

// Ultrasoon waardes
uint16_t counter = 0; // 16 bit counter value
uint8_t echo = 0; // a flag

// De array met taken
sTask scheduler_tasks[SCHEDULER_MAX_TASKS];

/* scheduler_dispatch_tasks()

Voert taak uit wanneer de taak aan de beurt is.
Roep de functie continu aan in main()

*/

void scheduler_dispatch_tasks(void)
{
   unsigned char index;

   // Voor taak uit als de taak aan de beurt is
   for(index = 0; index < SCHEDULER_MAX_TASKS; index++)
   {
      if((scheduler_tasks[index].RunMe > 0) && (scheduler_tasks[index].pTask != 0))
      {
         (*scheduler_tasks[index].pTask)();  // Voert taak uit
         scheduler_tasks[index].RunMe -= 1;   // Reset de taak

         // verwijderd eenmalige taken
         if(scheduler_tasks[index].Period == 0)
         {
            scheduler_delete_task(index);
         }
      }
   }
}

/* scheduler_add_task()

Voegt taak toe aan de scheduler

pFunction - De naam van de functie die als taak moet worden toegevoegd.
            NOTE: functie moet 'void function(void)' zijn dat betekent
            geen parameters en return type void.
                
DELAY     - DELAY voor dat de taak voor het eerst wordt uitgevoerd

PERIOD    - Periode waarin de taak moet worden uitgevoerd
            Als PERIOD == 0: Taak wordt eenmalig uitgevoerd
            Als PERIOD > 0: Taak wordt uitgevoerd een keer per PERIOD


RETURN VALUE:  

index - Geeft de positie van de taak in de array terug. 
Als index == SCHEDULER_MAX_TASK: Taak niet toegevoegd aan array
Als index < SCHEDULER_MAX_TASK: Taak toegevoegd aan array

*/

unsigned char scheduler_add_task(void (*pFunction)(), const unsigned int DELAY, const unsigned int PERIOD)
{
   unsigned char index = 0;

   // Zoekt naar een plaats voor de taak in de array
   while((scheduler_tasks[index].pTask != 0) && (index < SCHEDULER_MAX_TASKS))
   {
      index++;
   }

   // Controleert of er nog een taak in de array past 
   if(index == SCHEDULER_MAX_TASKS)
   {
      // Geen ruimte voor nieuwe taak in array
      return SCHEDULER_MAX_TASKS;  
   }

   // Taak in de array plaatsen
   scheduler_tasks[index].pTask = pFunction;
   scheduler_tasks[index].Delay =DELAY;
   scheduler_tasks[index].Period = PERIOD;
   scheduler_tasks[index].RunMe = 0;

   // return positie van taak in array
   return index;
}


/* scheduler_delete_task()

Verwijderd taak uit de scheduler. Dit verwijderd de functie niet van het geheugen,
maar de taak wordt niet meer uitgevoerd door de scheduler
 
TASK_INDEX - Taak index: gegeven door scheduler_add_task(). 
*/

void scheduler_delete_task(const unsigned char TASK_INDEX)
{
   scheduler_tasks[TASK_INDEX].pTask = 0;
   scheduler_tasks[TASK_INDEX].Delay = 0;
   scheduler_tasks[TASK_INDEX].Period = 0;
   scheduler_tasks[TASK_INDEX].RunMe = 0;
}

/* scheduler_init_timer1()

  Instellen van de timer1: Prescaler, Compare Register, CTC mode.
  Deze funcie roep je aan voor het gebruiken van de scheduler.  

*/

void scheduler_init_timer1(void)
{
   unsigned char i;
   // verwijderd taken als er meer zijn als het maximale toegestaande taken
   for(i = 0; i < SCHEDULER_MAX_TASKS; i++)
   {
      scheduler_delete_task(i);
   }

   // Instellingen voor Timer 1 (10 ms):
   OCR1A = (uint16_t)625;   		     // 10ms = (256/16.000.000) * 625
   TCCR1B = (1 << CS12) | (1 << WGM12);  // prescale op 256, top counter = value OCR1A (CTC mode)
   TIMSK1 = 1 << OCIE1A;   		     // Timer 1 Output Compare A Match Interrupt Enable
}

/* scheduler_start()

start de scheduler door interrupts aan te zetten

*/

void scheduler_start(void)
{
      sei();
}

/* schudeler_update

Dit is de scheduler ISR (update). Het wordt aangeroepen 
op basis van de instellingen in scheduler_init_timer1().

*/

ISR(TIMER1_COMPA_vect)
{
   unsigned char index;
   for(index = 0; index < SCHEDULER_MAX_TASKS; index++)
   {
      // Controleert of een taak op index in array aanwezig is
      if(scheduler_tasks[index].pTask)
      {
         if(scheduler_tasks[index].Delay == 0)
         {
            // Taak is klaar om uitgevoerd te worden, inc 'RunMe' flag 
            scheduler_tasks[index].RunMe += 1;

            if(scheduler_tasks[index].Period)
            {
               // periodieke taken opnieuw instellen
               scheduler_tasks[index].Delay = scheduler_tasks[index].Period;
               scheduler_tasks[index].Delay -= 1;
            }
         }
         else
         {
            // Verlaag Delay als taak niet klaar is om uitgevoerd te worden
            scheduler_tasks[index].Delay -= 1;
         }
      }
   }
}

// init functies
void init_ports(void)
{
    // set pin PB5 (arduino: 13) as output for GREEN LED
    // set pin PB4 (arduino: 12) as output for RED LED
    // set pin PB3 (arduino: 11) as output for YELLOW LED
    DDRB |= 0b00111000;
    // set pin PB1 (arduino: 9) as output for motor (reversed)
    // set pin PB0 (arduino: 8) as output for motor
    DDRB |= 0b00000011;
    // set pin PD4 (arduino: 4) as output for Trigger Ultrasoonsensor
    DDRD |= 0b00010000;
    // set pin PD3 (arduino: 3) as input for Echo Ultrasoonsensor
    DDRD &= 0b11110111;

}


void init_ext_int1(void)
{
    // Voor lezen Echo van Ultrasoonsensor
    // any change triggers ext interrupt 1
    EICRA = (1 << ISC10);
    EIMSK = (1 << INT1);
}

void init_timer0()
{
    TCCR0A = 0;
    TCCR0B = 0;
    TIMSK0 = (1<<TOIE0);
}


void init_uart(void)
{
	// baud rate
    uint8_t UBBRVAL = 51;
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// set transmitter en receiver aan
	UCSR0B = (1<<TXEN0) | (1<<RXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = (1<<UCSZ01) | (1<<UCSZ00);
}

// uart functies 
void transmit(uint8_t data)
{
	// wacht totdat transmit buffer leeg is
	// UDRE wordt gezet wanneer de transmit buffer leeg is
	loop_until_bit_is_set(UCSR0A, UDRE0);
	// zet dat in UDR
	UDR0 = data;
}

uint8_t receive(void)
{
	// wacht totdat er data op de recieve buffer wordt gezet 
    // RXC0 wordt gezet wanneer de er data in de recieve buffer staat
    loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}

// Ultrasoon functies
ISR (INT1_vect)
{
    echo = (~echo) & 1;
	if (echo){
		start_timer();
	} else {
		init_timer0();
	}
}

ISR (TIMER0_OVF_vect)
{
    counter++;
}

void start_timer()
{
    TCNT0 = 0;
    counter = 0;
    TCCR0B = (1<<CS01) | (1<<CS00);
}

void send_trigger(void)
{
	_delay_ms(50);		//Restart HC-SR04
	PORTD &=~ (1 << PIND4);
	_delay_us(1);
	PORTD |= (1 << PIND4); //Send 10us second pulse
	_delay_us(10);
	PORTD &=~ (1 << PIND4);
}

uint16_t calc_cm(uint16_t counter)
{
    uint16_t result = (counter * 256 + TCNT0) * 4 / 58;
	return result;
}

// LED functies
void turn_on_green_led(void)
{
    PORTB |= 0b00100000;
}

void turn_off_green_led(void)
{
    PORTB &= 0b11011111;
}

void turn_on_red_led(void)
{
    PORTB |= 0b00010000;
}

void turn_off_red_led(void)
{
    PORTB &= 0b11101111;
}

void turn_on_yellow_led(void)
{
    PORTB |= 0b00001000;
}

void turn_off_yellow_led(void)
{
    PORTB &= 0b11110111;
}

// Motor functies
void start_motor(void)
{
    //zorgt er voor dat motor niet in reverse draait
    PORTB &= 0b11111101;
    //start motor 
    PORTB |= 0b00000001;
}

void start_motor_reversed(void)
{
    //zorgt er voor dat motor niet draait
    PORTB &= 0b11111110;
    //start motor in reverse
    PORTB |= 0b00000010;
}

void stop_motor(void)
{
    //zorgt er voor dat motor stopt met draaien
    PORTB &= 0b11111100; 
}

int main()
{
	//init
    init_ports();
    init_uart();
    init_ext_int1();
    init_timer0();
	scheduler_init_timer1();
    // tasks
    scheduler_add_task(turn_on_red_led,0,400);
    scheduler_add_task(turn_off_red_led,200,400);
    // start de scheduler
	scheduler_start();
	while (1) {
		//scheduler_dispatch_tasks();
        send_trigger();
		_delay_ms(1000);
		uint8_t distance = calc_cm(counter);
		transmit(distance);
	}

	return(0);
}


