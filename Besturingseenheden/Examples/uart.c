#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#define F_CPU 16E6

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

int main(void)
{
	init();
	DDRB = 0xFF;
	uint8_t data = 0;
	while (1) {
		data = receive();
		if (data) {
			PORTB = 0xFF;
			} else {
			PORTB = 0x00;
		}
	}
}


