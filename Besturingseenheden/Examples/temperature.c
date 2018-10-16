/*
 * temp.c
 *
 * Created: 08-Oct-18 13:06:12
 * Author : Mike
 */

#include <avr/io.h>
#define F_CPU 16E6
#include <util/delay.h>

#define HIGH 0x1
#define LOW 0x0

const uint8_t data = 0;
const uint8_t clock = 1;
const uint8_t strobe = 2;

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

void show_celsius(uint32_t celsius)
{
	/*0*/ /*1*/ /*2*/ /*3*/ /*4*/ /*5*/ /*6*/ /*7*/ /*8*/ /*9*/
	uint8_t digits[] = {0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f};
	uint8_t ar[8] = {0};
	uint8_t digit = 0, i = 0;
	uint8_t temp, spaces;
	
	// cm=1234 -> ar[0..7] = {4,3,2,1,0,0,0,0}
	while (celsius > 0 && i < 8) {
		digit = celsius % 10;
		ar[i] = digit;
		celsius = celsius / 10;
		i++;
	}

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

void init_ports(void)
{
	DDRB |=  0xFF;
	DDRC &=~ (1 << PINC0);
}

void init_adc()
{
	// ref=Vcc, left adjust the result (8 bit resolution),
	// select channel 0 (PC0 = input)
	ADMUX = (1<<REFS0)|(1<<ADLAR);
	// enable the ADC & prescale = 128
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}

uint16_t get_adc_value()
{
	ADCSRA |= (1<<ADSC); // start conversion
	loop_until_bit_is_clear(ADCSRA, ADSC);
	return  ADCL / 64 + ADCH * 4; // 8-bit resolution, left adjusted
}

int main(void)
{
	init_ports();
	reset_display();
    init_adc();	while(1){		float v_out = (float) get_adc_value() * (5.0 / 1024.0);		uint16_t celsius = (uint16_t) ((v_out - 0.5) * 100);		show_celsius(celsius);
		_delay_ms(1000);
	}
}

