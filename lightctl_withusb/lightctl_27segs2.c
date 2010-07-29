/*
 *	This is version 0.2 of LightCTL. It controls the power of a lamp using
 *	a regulator board and a teensy board. It displays the voltage using a 
 *	series of 7 segment displays. Later versions will have more useful usb
 *	serial support. This one has very little or perhaps none.
 */

/* 
 *	It is copyright (c) Spencer Krum. July 17, 2010. It is released under the
 * 	GPL v3 or any later version.
 */

/*
 * 	This code draws on code written by others. See example teensy code at
 *	http://www.pjrc.com and example code at http://www.github.com/greghayn
 *	es/pdx-rov . It is used with permission.
 */


#include <avr/io.h>
#include <avr/pgmspace.h>
#include <stdint.h>
#include <util/delay.h>
#include "usb_serial.h"
#include "sampling.c"

#define CPU_PRESCALE(n) (CLKPR = 0x80, CLKPR = (n))
#define HEX(n) (((n) < 10) ? ((n) + '0') : ((n) + 'A' - 10))

uint8_t HIGHBIT;
uint8_t LOWBIT;



uint16_t read_sensor(void){
	uint16_t val;
	adc_start(ADC_MUX_PIN_F0, ADC_REF_POWER);
	val = adc_read();
	return val;
}

void set_display(uint16_t val)
{
	int val_ = val;
	uint8_t high, low;
	val /= 10;
	if (val_ > 99)
		val_ = 99;
		
	high = val_ / 10;
	low = (val_ - (high * 10));
	HIGHBIT = high;
	LOWBIT = low;
}


void display_num(uint8_t number)
{
	uint8_t full = 255;
	uint8_t off  = 0;
	switch(number)
	{
		case 0:
			OCR0B = off;
			OCR1A = off;
			OCR2A = off;
			OCR2B = off;
			break;
		case 1:
			OCR0B = off;
			OCR1A = off;
			OCR2A = off;
			OCR2B = full;
			break;
		case 2:
			OCR0B = off;
			OCR1A = off;
			OCR2A = full;
			OCR2B = off;
			break;
		case 3:
			OCR0B = off;
			OCR1A = off;
			OCR2A = full;
			OCR2B = full;
			break;
		case 4:
			OCR0B = full;
			OCR1A = off;
			OCR2A = off;
			OCR2B = off;
			break;
		case 5:
			OCR0B = full;
			OCR1A = off;
			OCR2A = off;
			OCR2B = full;
			break;
		case 6:
			OCR0B = full;
			OCR1A = off;
			OCR2A = full;
			OCR2B = off;
			break;
		case 7:
			OCR0B = full;
			OCR1A = off;
			OCR2A = full;
			OCR2B = full;
			break;
		case 8:
			OCR0B = off;
			OCR1A = full;
			OCR2A = off;
			OCR2B = off;
			break;
		case 9:
			OCR0B = off;
			OCR1A = full;
			OCR2A = off;
			OCR2B = full;
			break;
		case 10:
			OCR0B = off;
			OCR1A = off;
			OCR2A = off;
			OCR2B = off;
			break;
		case 11:
			OCR0B = off;
			OCR1A = off;
			OCR2A = off;
			OCR2B = off;
			break;
		case 12:
			OCR0B = off;
			OCR1A = off;
			OCR2A = off;
			OCR2B = off;
			break;
		case 13:
			OCR0B = off;
			OCR1A = off;
			OCR2A = off;
			OCR2B = off;
			break;
		case 14:
			OCR0B = off;
			OCR1A = off;
			OCR2A = off;
			OCR2B = off;
			break;
		case 15:
			OCR0B = off;
			OCR1A = off;
			OCR2A = off;
			OCR2B = off;
			break;
		case 16:
			OCR0B = off;
			OCR1A = off;
			OCR2A = off;
			OCR2B = off;
			break;					 	
	}
}

void display(void){
	uint8_t full = 255;
	uint8_t off = 0;
	int delay = 2;
	
	OCR0A = full;
	display_num(HIGHBIT);
	_delay_ms(delay);
	OCR0A = off;
	display_num(LOWBIT);
	_delay_ms(delay);
}


void set_default_duty_cycles(void)
{
	
	//TODO figure out what the f*** is going on here
	OCR0A = 0x00;
	OCR0B = 0x00;
	
	OCR2A = 0x00;
	OCR2B = 0x00;
	
	OCR1AH = 0x00;
	OCR1AL = 0x00; // Register used by 8 bit pwm
	OCR1BH = 0x00;
	OCR1BL = 0x00; // Register used by 8 bit pwm
	OCR1CL = 0x00;
	OCR1CL = 0x00; // Covered by OCR0A

	OCR3AH = 0x00;
	OCR3AL = 0x00; // Register used by 8 bit pwm
	OCR3BH = 0x00;
	OCR3BL = 0x00; // Register used by 8 bit pwm
	OCR3CH = 0x00;
	OCR3CL = 0x00; // Register used by 8 bit pwm

	set_default_duty_cycles();
}


void setup_pwms(void)
{
	//TODO figure out what the f*** is going on here
	//TODO become a bittwidddling mastah

	// Timer 0
	// Set ports to output
	DDRB |= (1 << DDB4) | (1 << DDB5) | (1 << DDB6) | (1 << DDB7);
//	DDRC |= (1 << DDC4) | (1 << DDC5) | (1 << DDC6);
	DDRD |= (1 << DDD0) | (1 << DDD1);

	TCCR0A = (1 << COM0A1) | (1 << COM0B1) | (1 << WGM00) | (1 << WGM01);
	TCCR0B = (1 << CS00);

	TCCR2A = (1 << COM2A1) | (1 << COM2B1) | (1 << WGM20) | (1 << WGM21);
	TCCR2B = (1 << CS20);

	TCCR1A = (1 << COM1A1) | (1 << COM1B1) | (1 << WGM10);
	TCCR1B = (1 << WGM12) | (1 << CS10);
	TCCR1C = 0;

	TCCR3A = (1 << COM3A1) | (1 << COM3B1) | (1 << WGM30);
	TCCR3B = (1 << WGM32) | (1 << CS30);
	TCCR3C = 0;
}

int main(void)
{
	uint16_t val;

	CPU_PRESCALE(2); //why?
	setup_pwms();  
	
	while(1){
		val = read_sensor();
		set_display(val);
		display();
	}
}	
	





				

	
