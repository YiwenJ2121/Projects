/*
 Rural Traffic Light System - A simplified Model Using GPIOx_ODR
*/
#include "stm32f4xx.h"
void delayMs(int n);
int main(void) {
RCC->AHB1ENR |= 5; /* enable GPIOA & GPIOC clock */
    
GPIOA->MODER &= 0xFFFFFFF0; /* set port A as Input */
GPIOC->MODER = 0x00000555; /* set port B as Output */
GPIOA->PUPDR = 5;  /* setup internal Vcc for A0 A1 */
    
while(1) {
GPIOC->ODR = 0x21;  /* NS-g, EW-r */
    delayMs(2000);
	
/* check if EW has car */
while((GPIOA->IDR & 0x00000001) == 1)
{}
    
GPIOC->ODR = 0x22;  /* NS-y, EW-r */
    delayMs(1000);
    
GPIOC-> ODR = 0x0C;  /* NS-r, EW-g */
    delayMs(2000);
	
/* check if NS has car */
while((GPIOA->IDR & 0x00000002) == 2)
{}
    
GPIOC-> ODR = 0x14;  /* NS-r, EW-y */
    delayMs(1000);
}
}
/* 16 MHz SYSCLK */
void delayMs(int n) {
int i;
for (; n > 0; n--)
for (i = 0; i < 799; i++) ;
}


