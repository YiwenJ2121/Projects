/*
 Rural Traffic Light System - A simplified Model Using GPIOx_ODR
*/
#include "stm32f4xx.h"
void delayMs(int n);
int main(void) {
	RCC->AHB1ENR |= 5; /* enable GPIOA & GPIOC clock */
	GPIOA->MODER &= 0xFFFFFFF0; /* set port A as Input */
	GPIOC->MODER = 0x00005555; /* set port B as Output */
  GPIOA->PUPDR = 0x00000001;   /*setup internal Vcc for A0 A1 */

	int something[] = {0x00, 0x3f, 0x00, 0x3f, 0x00, 0x3f, 0x06, 0x5b, 0x4f, 0x66, 0x6d, 0x7d, 0x07, 0x7f, 0x6f}; 
	int i; 
	while (1)
	{
		while ((GPIOA->IDR & 0x00000001) == 0x00)	
		{
			for(i = 14; i>=0; i--) 
			{
				GPIOC->ODR = something[i];           
				delayMs(500);
			}		 
		}
	}
}
/* 16 MHz SYSCLK */
void delayMs(int n) {
	int i;
	for (; n > 0; n--)
		for (i = 0; i < 799; i++) ;
}


