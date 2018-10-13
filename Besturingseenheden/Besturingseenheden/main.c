#include "const.h"
#include "scheduler.h"
#include <avr/interrupt.h>
#include <avr/io.h>
#include <stdint.h>
#include <util/delay.h>


// Array met de sensorwaarden
uint8_t sensor_values[5];

// The array of tasks
sTask scheduler_tasks[SCHEDULER_MAX_TASKS];


/*------------------------------------------------------------------*-

  scheduler_dispatch_tasks()

  This is the 'dispatcher' function.  When a task (function)
  is due to run, scheduler_dispatch_tasks() will run it.
  This function must be called (repeatedly) from the main loop.

-*------------------------------------------------------------------*/

void scheduler_dispatch_tasks(void)
{
   unsigned char Index;

   // Dispatches (runs) the next task (if one is ready)
   for(Index = 0; Index < SCHEDULER_MAX_TASKS; Index++)
   {
      if((scheduler_tasks[Index].RunMe > 0) && (scheduler_tasks[Index].pTask != 0))
      {
         (*scheduler_tasks[Index].pTask)();  // Run the task
         scheduler_tasks[Index].RunMe -= 1;   // Reset / reduce RunMe flag

         // Periodic tasks will automatically run again
         // - if this is a 'one shot' task, remove it from the array
         if(scheduler_tasks[Index].Period == 0)
         {
            scheduler_delete_task(Index);
         }
      }
   }
}

/*------------------------------------------------------------------*-

  scheduler_add_task()

  Causes a task (function) to be executed at regular intervals 
  or after a user-defined delay

  pFunction - The name of the function which is to be scheduled.
              NOTE: All scheduled functions must be 'void, void' -
              that is, they must take no parameters, and have 
              a void return type. 
                   
  DELAY     - The interval (TICKS) before the task is first executed

  PERIOD    - If 'PERIOD' is 0, the function is only called once,
              at the time determined by 'DELAY'.  If PERIOD is non-zero,
              then the function is called repeatedly at an interval
              determined by the value of PERIOD (see below for examples
              which should help clarify this).


  RETURN VALUE:  

  Returns the position in the task array at which the task has been 
  added.  If the return value is SCHEDULER_MAX_TASKS then the task could 
  not be added to the array (there was insufficient space).  If the
  return value is < SCHEDULER_MAX_TASKS, then the task was added 
  successfully.  

  Note: this return value may be required, if a task is
  to be subsequently deleted - see scheduler_delete_task().

  EXAMPLES:

  Task_ID = scheduler_add_task(Do_X,1000,0);
  Causes the function Do_X() to be executed once after 1000 sch ticks.            

  Task_ID = scheduler_add_task(Do_X,0,1000);
  Causes the function Do_X() to be executed regularly, every 1000 sch ticks.            

  Task_ID = scheduler_add_task(Do_X,300,1000);
  Causes the function Do_X() to be executed regularly, every 1000 ticks.
  Task will be first executed at T = 300 ticks, then 1300, 2300, etc.            
 
-*------------------------------------------------------------------*/

unsigned char scheduler_add_task(void (*pFunction)(), const unsigned int DELAY, const unsigned int PERIOD)
{
   unsigned char Index = 0;

   // First find a gap in the array (if there is one)
   while((scheduler_tasks[Index].pTask != 0) && (Index < SCHEDULER_MAX_TASKS))
   {
      Index++;
   }

   // Have we reached the end of the list?   
   if(Index == SCHEDULER_MAX_TASKS)
   {
      // Task list is full, return an error code
      return SCHEDULER_MAX_TASKS;  
   }

   // If we're here, there is a space in the task array
   scheduler_tasks[Index].pTask = pFunction;
   scheduler_tasks[Index].Delay =DELAY;
   scheduler_tasks[Index].Period = PERIOD;
   scheduler_tasks[Index].RunMe = 0;

   // return position of task (to allow later deletion)
   return Index;
}

/*------------------------------------------------------------------*-

  scheduler_delete_task()

  Removes a task from the scheduler.  Note that this does
  *not* delete the associated function from memory: 
  it simply means that it is no longer called by the scheduler. 
 
  TASK_INDEX - The task index.  Provided by scheduler_add_task(). 

  RETURN VALUE:  RETURN_ERROR or RETURN_NORMAL

-*------------------------------------------------------------------*/

unsigned char scheduler_delete_task(const unsigned char TASK_INDEX)
{
   // Return_code can be used for error reporting, NOT USED HERE THOUGH!
   unsigned char Return_code = 0;

   scheduler_tasks[TASK_INDEX].pTask = 0;
   scheduler_tasks[TASK_INDEX].Delay = 0;
   scheduler_tasks[TASK_INDEX].Period = 0;
   scheduler_tasks[TASK_INDEX].RunMe = 0;

   return Return_code;
}

/*------------------------------------------------------------------*-

  scheduler_init_timer1()

  Scheduler initialisation function.  Prepares scheduler
  data structures and sets up timer interrupts at required rate.
  You must call this function before using the scheduler.  

-*------------------------------------------------------------------*/

void scheduler_init_timer1(void)
{
   unsigned char i;

   for(i = 0; i < SCHEDULER_MAX_TASKS; i++)
   {
      scheduler_delete_task(i);
   }

   // Set up Timer 1
   // Values for 1ms and 10ms ticks are provided for various crystals

   // Hier moet de timer periode worden aangepast ....!
   OCR1A = (uint16_t)625;   		     // 10ms = (256/16.000.000) * 625
   TCCR1B = (1 << CS12) | (1 << WGM12);  // prescale op 64, top counter = value OCR1A (CTC mode)
   TIMSK1 = 1 << OCIE1A;   		     // Timer 1 Output Compare A Match Interrupt Enable
}

/*------------------------------------------------------------------*-

  scheduler_start()

  Starts the scheduler, by enabling interrupts.

  NOTE: Usually called after all regular tasks are added,
  to keep the tasks synchronised.

  NOTE: ONLY THE SCHEDULER INTERRUPT SHOULD BE ENABLED!!! 
 
-*------------------------------------------------------------------*/

void scheduler_start(void)
{
      sei();
}

/*------------------------------------------------------------------*-

  schudele_update

  This is the scheduler ISR.  It is called at a rate 
  determined by the timer settings in scheduler_init_timer1().

-*------------------------------------------------------------------*/

ISR(TIMER1_COMPA_vect)
{
   unsigned char Index;
   for(Index = 0; Index < SCHEDULER_MAX_TASKS; Index++)
   {
      // Check if there is a task at this location
      if(scheduler_tasks[Index].pTask)
      {
         if(scheduler_tasks[Index].Delay == 0)
         {
            // The task is due to run, Inc. the 'RunMe' flag
            scheduler_tasks[Index].RunMe += 1;

            if(scheduler_tasks[Index].Period)
            {
               // Schedule periodic tasks to run again
               scheduler_tasks[Index].Delay = scheduler_tasks[Index].Period;
               scheduler_tasks[Index].Delay -= 1;
            }
         }
         else
         {
            // Not yet ready to run: just decrement the delay
            scheduler_tasks[Index].Delay -= 1;
         }
      }
   }
}

// init functies
void init_ports()
{
    // set pin B3 - B5 (arduino: 11 - 13) as output for leds
    DDRB |= 0b00111000;
    // set pin B0 (arduino: 8) as output & B1 (arduino: 9) as input
    // for ultrasoonsensor
    DDRB |= 0b00000001;
    DDRB &= 0b11111101;
    // set pin C0 - C4 (arduino: A0 - A4) as input for sensors
    DDRC &= 0b11100000;
    
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
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
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

uint8_t receive(void)
{
	// wacht totdat er data op de recieve buffer wordt gezet 
    // RXC0 wordt gezet wanneer de er data in de recieve buffer staat
    loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}

//sensor functies
uint8_t get_adc_value()
{
	ADCSRA |= (1<<ADSC); // start conversion
	loop_until_bit_is_clear(ADCSRA, ADSC);
	return ADCH; // 8-bit resolution, left adjusted
}

void read_sensor0(void)
{
    // zet channel van adc op PC0
    ADMUX &= 11110000;
    // slaat adc value op in sensor_values array 
    sensor_values[0] = get_adc_value();
}

void transmit_sensor_values()
{
    for (int i = 0; i < 5; i++){
        transmit(sensor_values[i]);
    }
}

int main()
{
	init_ports();
    init_uart();
    init_adc();
	scheduler_init_timer1(); // init de timer en verwijder alle taken
	scheduler_add_task(read_sensor0,0,100);
    scheduler_add_task(transmit_sensor_values,0,500);
	scheduler_start(); // start de scheduler
	while (1) {
		scheduler_dispatch_tasks();
	}

	return(0);
}
