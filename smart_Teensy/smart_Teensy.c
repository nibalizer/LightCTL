/*
 *	This is version 0.2 of LightCTL. It controls the power of a lamp using
 *	a regulator board and a teensy board. It displays the voltage using a 
 *	series of 7 segment displays. Later versions will have more useful usb
 *	serial support. This one has very little or perhaps none.
 */

/*
 *  Project website at http://github.com/spencer-krum/LightCTL
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

#define DIGITAL_IO_INIT_D	(DDRB  |= (1<<0)|(1<<1)|(1<<2)|(1<<3)) //Set pins B0 - B3 as digital outputs
#define DITITAL_IO_INIT_C	(DDRC |= (1<<7)

void send_str(const char *s);
uint8_t recv_str(char *but, uint8_t size);
	
int lowerloop = 1;

/*
 * command to perform ADC on a sensor port(F0-F7)
 */


uint16_t read_sensor(uint8_t sensor)
{
	uint16_t val;

	adc_start(sensor, ADC_REF_POWER);

	val = adc_read();
	usb_serial_putchar(val);
	return val;
	
}

/*
 * command to output to and multiplex accross seven segment displays
 */


void set_display(uint16_t val)
{
	int val_ = val;
	uint8_t high, low;
	if (val_ > 990)
		val_ = 990;
	
	val_ /= 10;
	high = val_ / 10;
	low = (val_ - (high * 10));

	PORTC |= (1<<7);	
	PORTB = high;
	PORTC &= ~(1<<7);
	PORTB = low;
}


void lamp_v(uint8_t lum){
	OCR1B = lum;
}
	


void set_default_duty_cycles(void)
{
	
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


uint16_t PID(uint16_t pot, uint16_t lux)
{
    //constants
    uint8_t kp; //proportional constant
    uint8_t ki; //integral constant
    uint8_t kd; //derivative constant


    uint16_t ratio;
	ratio = pot/lux;

    uint16_t difference;
    difference = pot - lux;

	uint16_t pid;

    uint16_t proportion;
    proportion = difference * kp;

	return pid;
}

void handle_set_pwm_command(uint8_t port, uint8_t val)
{
	switch(port)
	{
		case 0:
			OCR0A = val;
			break;
		case 1:
			OCR0B = val;
			break;
		case 2:
			OCR1A = val;
			break;
		case 3:
			OCR1B = val;
			break;
		case 4:
			OCR2A = val;
			break;
		case 5:
			OCR2B = val;
			break;
		case 6:
			OCR3A = val;
			break;
		case 7:
			OCR3B = val;
			break;
		case 8:
			OCR3C = val;
			break;
		default:
			return;
	}
	usb_serial_putchar('\x00');
	usb_serial_putchar('\n');
}
void setup_digitalio(void)
{
    
    DDRB  |= (1<<0)|(1<<1)|(1<<2)|(1<<3);   //Set pins B0 - B3 as digital outputs
    DDRC  |= (1<<7);                        //Set pin C7 as didigal output

}


/**
 * @breif Handle a set digital I/O command
 */


void handle_set_digitalio_command(uint8_t port, uint8_t val)
{
	usb_serial_putchar('\x09');
	usb_serial_putchar(port);
	//This part is from the CS tutors, Jesusaurus++
	if (val)
	{
		PORTB |= (1 << port);
	}else{
		PORTB &= ~(1 << port);
	}


	usb_serial_putchar('\x00');
	usb_serial_putchar('\n');
}

void lowerhalf(uint8_t onoff)
{
	usb_serial_putchar('\x00');
    if (onoff){
		lowerloop = 1;
        usb_serial_putchar('\x00');
        usb_serial_putchar('\n');
	}else{
		lowerloop = 0;
        usb_serial_putchar('\x01');
        usb_serial_putchar('\n');
	}	
}

void handle_command(const char *str, uint8_t len)
{
	if(len == 0)
		return;

	switch(str[0])
	{
		case 0:
			lowerhalf(str[1]);
			break;
		
		case 4:
			handle_set_pwm_command(str[1], str[2]);
			break;
       
        case 7:
            read_sensor(str[1]);
           	break;
		
        case 9:
			handle_set_digitalio_command(str[1], str[2]);
			break;	
		
        default:
			send_str(PSTR("INVALID_COMMAND_CODE"));
	}
}


int main(void)
{
	uint16_t lux, pot, pid;
	uint8_t n;
    uint8_t F0 = 0x00;
    uint8_t F1 = 0x01;
	char buf[32];	    


	CPU_PRESCALE(2); //why?
	setup_pwms();  

	usb_init();
	while (!usb_configured());
	_delay_ms(1000);



	while(1){
		while (!(usb_serial_get_control() & USB_SERIAL_DTR)) 
		usb_serial_flush_input();
		send_str(PSTR("Everything Initialized!"));
		while(1){
			//Upper Half
			n = recv_str(buf, sizeof(buf));
			if (n == 255) break;
			handle_command(buf, n);
		

			//Lower Half
			if (lowerloop){

				pot = read_sensor(F0); 
				lux = read_sensor(F1);
                set_display(lux);
				//pid = PID(lux, pot);
				//lamp_v(pid);
			}
		}
	}
}	

	


// Send a string to the USB serial port.  The string must be in
// flash memory, using PSTR
//
void send_str(const char *s)
{
	char c;
	while (1) {
		c = pgm_read_byte(s++);
		if (!c) break;
		usb_serial_putchar(c);
	}
}


// Receive a string from the USB serial port.  The string is stored
// in the buffer and this function will not exceed the buffer size.
// A carriage return or newline completes the string, and is not
// stored into the buffer.
// The return value is the number of characters received, or 255 if
// the virtual serial connection was closed while waiting.
//
uint8_t recv_str(char *buf, uint8_t size)
{
	int16_t r;
	uint8_t count=0;

	while (count < size) {
		r = usb_serial_getchar();
		if (r != -1) {
			if (r == '\r' || r == '\n') return count;
			*buf++ = r;
			//usb_serial_putchar(r);
			count++;
		} else {
			if (!usb_configured() ||
			  !(usb_serial_get_control() & USB_SERIAL_DTR)) {
				// user no longer connected
				return 255;
			}
			// just a normal timeout, keep waiting
		}
	}
	return count;
}


//  Live Long and Prosper - Spock
