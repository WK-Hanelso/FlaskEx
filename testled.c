#include<wiringPi.h>
#include<stdio.h>

#define LEDR 1
#define LEDY 4
#define LEDG 5

void ledControl( int pin, int mode );
void WGsetup();

int main()
{
	int gno;
	
	wiringPiSetup();
	printf("%d\n", LOW );

	ledControl( LEDR, HIGH );

	delay( 2000 );

	ledControl( LEDG, HIGH );

	delay( 2000 );

	ledControl( LEDY, HIGH );

	delay( 2000 );

	ledControl( LEDR, LOW );
	ledControl( LEDG, LOW );
	ledControl( LEDY, LOW );

	return 0;
}

void ledControl( int pin , int mode)
{
	int i = 0;

	pinMode( pin, OUTPUT );

	digitalWrite( pin, mode );
}

void WGsetup()
{
	wiringPiSetup();
}

