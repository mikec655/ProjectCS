#include "const.h"
#include "scheduler.h"
#include <avr/interrupt.h>
#include <avr/io.h>
#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <util/delay.h>

//average sensor_value
#define AMOUNT_OF_SENSOR_VALUES 20
int32_t sensor_values[AMOUNT_OF_SENSOR_VALUES];
uint8_t sensor_value_index = 0;

// De array met taken
sTask scheduler_tasks[SCHEDULER_MAX_TASKS];

//scheduler_dispatch_tasks()
//Voert taak uit wanneer de taak aan de beurt is.
//Roep de functie continu aan in main()


void scheduler_dispatch_tasks(void)
{
   unsigned char index;

   //Voor taak uit als de taak aan de beurt is
   for(index = 0; index < SCHEDULER_MAX_TASKS; index++)
   {
      if((scheduler_tasks[index].RunMe > 0) && (scheduler_tasks[index].pTask != 0))
      {
         (scheduler_tasks[index].pTask)();  // Voert taak uit
         scheduler_tasks[index].RunMe -= 1;  //  Reset de taak

         // verwijderd eenmalige taken
         if(scheduler_tasks[index].Period == 0)
         {
            scheduler_delete_task(index);
         }
      }
   }
}

 //scheduler_add_task()
//Voegt taak toe aan de scheduler
//pFunction - De naam van de functie die als taak moet worden toegevoegd.
            //NOTE functie moet 'void function(void)' zijn dat betekent
            //geen parameters en return type void.
                //
//DELAY     - DELAY voor dat de taak voor het eerst wordt uitgevoerd
//PERIOD    - Periode waarin de taak moet worden uitgevoerd
            //Als PERIOD == 0 Taak wordt eenmalig uitgevoerd
            //Als PERIOD  0 Taak wordt uitgevoerd een keer per PERIOD
//RETURN VALUE  
//index - Geeft de positie van de taak in de array terug. 
//Als index == SCHEDULER_MAX_TASK Taak niet toegevoegd aan array
//Als index  SCHEDULER_MAX_TASK Taak toegevoegd aan array


unsigned char scheduler_add_task(void (pFunction)(), const unsigned int DELAY, const unsigned int PERIOD)
{
   unsigned char index = 0;

   //Zoekt naar een plaats voor de taak in de array
   while((scheduler_tasks[index].pTask != 0) && (index < SCHEDULER_MAX_TASKS))
   {
      index++;
   }

   //Controleert of er nog een taak in de array past 
   if(index == SCHEDULER_MAX_TASKS)
   {
      //Geen ruimte voor nieuwe taak in array
      return SCHEDULER_MAX_TASKS;  
   }

   //Taak in de array plaatsen
   scheduler_tasks[index].pTask = pFunction;
   scheduler_tasks[index].Delay =DELAY;
   scheduler_tasks[index].Period = PERIOD;
   scheduler_tasks[index].RunMe = 0;

   //return positie van taak in array
   return index;
}


//scheduler_delete_task()
//Verwijderd taak uit de scheduler. Dit verwijderd de functie niet van het geheugen,
//maar de taak wordt niet meer uitgevoerd door de scheduler
 
//TASK_INDEX - Taak index gegeven door scheduler_add_task(). 


void scheduler_delete_task(const unsigned char TASK_INDEX)
{
   scheduler_tasks[TASK_INDEX].pTask = 0;
   scheduler_tasks[TASK_INDEX].Delay = 0;
   scheduler_tasks[TASK_INDEX].Period = 0;
   scheduler_tasks[TASK_INDEX].RunMe = 0;
}

//scheduler_delete_all_tasks()
//Verwijdert alle taken uit de scheduler.


void scheduler_delete_all_tasks()
{
	for (uint8_t i = 0; i < SCHEDULER_MAX_TASKS; i++){
		scheduler_delete_task(i);
	}
}


 //scheduler_init_timer1()
  //Instellen van de timer1 Prescaler, Compare Register, CTC mode.
  //Deze funcie roep je aan voor het gebruiken van de scheduler.  


void scheduler_init_timer1(void)
{
   unsigned char i;
   //verwijderd taken als er meer zijn als het maximale toegestaande taken
   for(i = 0; i < SCHEDULER_MAX_TASKS; i++)
   {
      scheduler_delete_task(i);
   }

   //Instellingen voor Timer 1 (10 ms)
   OCR1A = (uint16_t)625;   		     //10ms = (25616.000.000)  625
   TCCR1B = (1 << CS12) | (1 << WGM12);   //prescale op 256, top counter = value OCR1A (CTC mode)
   TIMSK1 = 1 << OCIE1A;   		      //Timer 1 Output Compare A Match Interrupt Enable
}

//scheduler_start()
//start de scheduler door interrupts aan te zetten


void scheduler_start(void)
{
      sei();
}

// schudeler_update
// Dit is de scheduler ISR (update). Het wordt aangeroepen 
// op basis van de instellingen in scheduler_init_timer1().


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
void init_ports()
{
     // set pin C0 (arduino A0) as input for TMP 36
    DDRC &= 0b11111110;
}

void init_uart()
{
	// baud rate
    uint8_t UBBRVAL = 51;
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// set transmitter en receiver aan
	UCSR0B = (1<<TXEN0) | (1<<RXEN0);
	// set frame format  asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = (1<<UCSZ01) | (1<<UCSZ00);
}

void init_adc()
{
	// ref=Vcc, left adjust the result (8 bit resolution),
	// select channel 0 (PC0 = input)
	ADMUX = (1<<REFS0) | (1<<ADLAR);
	// enable the ADC & prescale = 128
	ADCSRA = (1<<ADEN) | (1<<ADPS2) | (1<<ADPS1) | (1<<ADPS0);
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

void transmit_string(char* data)
{
	for (uint8_t i = 0; i < strlen(data); i++){
		transmit(data[i]);
	}
}

uint8_t receive(void)
{
	//wacht totdat er data op de recieve buffer wordt gezet 
    //RXC0 wordt gezet wanneer de er data in de recieve buffer staat
    loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}

void receive_string(char * data){
	uint8_t i = 0;
	strcpy(data, "");
	char c = receive();
	while (c != '\n') {
		data[i] = c;
		i++;
		c = receive();
	}
}

void transmit_sensor_value(void);
void save_sensor_value(void);

void init_connection(void) {
    char type[16] = "_LGHT\n";
	transmit_string(type);
    char response[16] = "";
    receive_string(response);
    if (strcmp(response, "_CONN") == 0) {
		scheduler_add_task(save_sensor_value, 0, 50);
        scheduler_add_task(transmit_sensor_value, 1000, 1000);
    } else {
		scheduler_add_task(init_connection, 0, 0);
	}
}

//sensor functies
uint16_t get_adc_value()
{
	ADCSRA |= (1<<ADSC);  //start conversion
	loop_until_bit_is_clear(ADCSRA, ADSC);
	// 10-bit resolution, left adjusted
	return ADCL / 64 + ADCH * 4; //ADCL has to be first!
}

void save_sensor_value()
{
	// rekent waarde om naar lux
    float v_out = (float) get_adc_value() * 0.00488281;
	float r_ldr = (10.0 * (5.0 - v_out)) / v_out;
	float lux = 500 / r_ldr;
    // sla lux waarde op in een array
	sensor_values[sensor_value_index] = lux;
	sensor_value_index += 1;
	sensor_value_index %= AMOUNT_OF_SENSOR_VALUES;
}

void transmit_sensor_value()
{
    // rekent de gem. uit van alle waardes in de array
	float sum = 0;
    for (uint8_t i = 0; i < AMOUNT_OF_SENSOR_VALUES; i++){
		sum += sensor_values[i];
	}
	float result = sum / AMOUNT_OF_SENSOR_VALUES; 
    // verstuurt waarde over serial
    char data[32];
	char formatted_result[16];
	dtostrf(result, 6, 1, formatted_result);
	sprintf(data, "_LGHT: %s\n", formatted_result);
	transmit_string(data);
}

void wait_for_task(void)
{
	char task[16] = "";
	receive_string(task);
    // init
    if (strcmp(task, "_INIT") == 0) {
        scheduler_add_task(init_connection, 0, 0);
	} else {
		scheduler_add_task(wait_for_task, 0, 0);
	}
}

int main()
{
	// init
    init_ports();
    init_uart();
    init_adc();
	scheduler_init_timer1();
    // tasks
    scheduler_add_task(wait_for_task,10,0);
    // start de scheduler
	scheduler_start();
	while (1) {
		scheduler_dispatch_tasks();
	}

	return(0);
}