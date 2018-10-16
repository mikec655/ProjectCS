/* 
 * HC-SR04
 * trigger to sensor : uno 0 (PD0) output
 * echo from sensor  : uno 3 (PD3 = INT1) input
 * 
 * DIO : uno 8  (PB0) data
 * CLK : uno 9  (PB1) clock
 * STB : uno 10 (PB2) strobe
 *
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#define F_CPU 16E6
#include <util/delay.h>
#include "distance.h"

volatile uint16_t gv_counter = 0; // 16 bit counter value
volatile uint8_t gv_echo = 0; // a flag

//********** start display ***********

void reset_display()
{
    // clear memory - all 16 addresses
    sendCommand(0x40); // set auto increment mode
    write(strobe, LOW);
    shiftOut(0xc0);   // set starting address to 0
    for(uint8_t i = 0; i < 16; i++)
    {
        shiftOut(0x00);
    }
    write(strobe, HIGH);
    sendCommand(0x89);  // activate and set brightness to medium
}

void show_distance(uint16_t cm)
{
                        /*0*/ /*1*/ /*2*/ /*3*/ /*4*/ /*5*/ /*6*/ /*7*/ /*8*/ /*9*/
    uint8_t digits[] = {0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f};
    uint8_t ar[8] = {0};
    uint8_t digit = 0, i = 0;
    uint8_t temp, nrs, spaces;
    
    // cm=1234 -> ar[0..7] = {4,3,2,1,0,0,0,0}
    while (cm > 0 && i < 8) {
        digit = cm % 10;
        ar[i] = digit;
        cm = cm / 10;
        i++;
    }

    nrs = i;      // 4 digits
    spaces = 8-i; // 4 leading spaces  
    
    // invert array -> ar[0..7] = {0,0,0,0,1,2,3,4}
    uint8_t n = 7;
    for (i=0; i<4; i++) {
        temp = ar[i];
        ar[i] = ar[n];
        ar[n] = temp;
        n--;
    }
    
    write(strobe, LOW);
    shiftOut(0xc0); // set starting address = 0
    // leading spaces
    for (i=0; i<8; i++) {
        if (i < spaces) {
            shiftOut(0x00);
        } else {
            shiftOut(digits[ar[i]]);
        }           
        shiftOut(0x00); // the dot
    }
    
    write(strobe, HIGH);
}

void sendCommand(uint8_t value)
{
    write(strobe, LOW);
    shiftOut(value);
    write(strobe, HIGH);
}

// write value to pin
void write(uint8_t pin, uint8_t val)
{
    if (val == LOW) {
        PORTB &= ~(_BV(pin)); // clear bit
    } else {
        PORTB |= _BV(pin); // set bit
    }
}

// shift out value to data
void shiftOut (uint8_t val)
{
    uint8_t i;
    for (i = 0; i < 8; i++)  {
        write(clock, LOW);   // bit valid on rising edge
        write(data, val & 1 ? HIGH : LOW); // lsb first
        val = val >> 1;
        write(clock, HIGH);
    }
}

//********** end display ***********

void init_ports(void)
{
	DDRB |=  0xFF;
	DDRD &=~ (1 << PIND3);
	DDRD |= (1 << PIND0);
}

void init_timer(void)
// prescaling : max time = 2^16/16E6 = 4.1 ms, 4.1 >> 2.3, so no prescaling required
// normal mode, no prescale, stop timer
{
    TCCR1A = 0;
    TCCR1B = 0;
	TIMSK1 |= _BV(TOIE1);
}

void start_timer(void)
{
	TCNT1 = 0;
	gv_counter = 0;
	TCCR1B |= _BV(CS10);
}

void init_ext_int(void)
{
    // any change triggers ext interrupt 1
    EICRA = (1 << ISC10);
    EIMSK = (1 << INT1);
}

void send_trigger(void)
{
	_delay_ms(50);		//Restart HC-SR04
	PORTD &=~ (1 << PIND0);
	_delay_us(1);
	PORTD |= (1 << PIND0); //Send 10us second pulse
	_delay_us(10);
	PORTD &=~ (1 << PIND0);
}


uint16_t calc_cm(uint16_t counter)
{
    uint16_t result = (counter * 65536 + TCNT1) / (58 * 16);
	return result;
}

int main(void)
{
	init_ext_int();
	init_timer();
	init_ports();
	reset_display();
	show_distance(2468);
	sei();
	while(1){
		send_trigger();
		_delay_ms(50);
		uint16_t distance = calc_cm(gv_counter);
		show_distance(distance);
	}
    return 0;
}

ISR (INT1_vect)
{
    gv_echo = (~gv_echo) & 1;
	if (gv_echo){
		start_timer();
	} else {
		init_timer();
		
	}
}

ISR (TIMER1_OVF_vect)
{
	gv_counter++;
}