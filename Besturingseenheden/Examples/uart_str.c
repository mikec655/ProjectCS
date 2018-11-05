#include <avr/io.h>
#include <stdlib.h>
#include <stdio.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6
#include <util/delay.h>
#include <string.h>

// output on USB = PD1 = board pin 1
// datasheet p.190; F_OSC = 16 MHz & baud rate = 19.200
#define UBBRVAL 51
void init()
{
	// set the baud rate
	UBRR0H = 0;
	UBRR0L = UBBRVAL;
	// disable U2X mode
	UCSR0A = 0;
	// enable transmitter and receiver
	UCSR0B = _BV(TXEN0) | _BV(RXEN0);
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
}
void transmit(uint8_t data)
{
	// wait for an empty transmit buffer
	// UDRE is set when the transmit buffer is empty
	loop_until_bit_is_set(UCSR0A, UDRE0);
	// send the data
	UDR0 = data;
}

uint8_t receive(void)
{
	loop_until_bit_is_set(UCSR0A, RXC0);
	return UDR0;
}

void transmit_string(char* data)
{
	for (uint8_t i = 0; i < strlen(data); i++){
		transmit(data[i]);
	}
}

void recieve_string(char* data){
	uint8_t i = 0;
	*data = '\0';
	char c = receive();
	while (c != '\n') {
		data[i] = c;
		i++;
		c = receive();
	}
}

int main(void)
{
	init();
	DDRB = 0xFF;
	while (1) {
		char string[16];
		sprintf(string, "TEMP: %d\n", 14);
		transmit_string(string);
		_delay_ms(1000);
	}
}