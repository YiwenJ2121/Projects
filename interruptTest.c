
#include "stm32f4xx.h"

void CountDown(void);
void EXTI15_10_IRQHandler(void);
void delayMs(int n);

int pressed = 0; /*added*/


int main(void) {
    __disable_irq();                    /* global disable IRQs */

	  RCC->AHB1ENR |= 7; /* enable GPIOA & GPIOC clock */

    RCC->APB2ENR |= 0x4000;             /* enable SYSCFG clock */
	
	

    /* configure PA5 for LED */
    GPIOA->MODER &= 0xFF5555FF;        /* clear pin mode */
    GPIOA->MODER |= 0x00555500; 					/* set port A as Output */
	
		/* Comfig PB0,2,4,6,8,9 for output (Traffic lights) */
		GPIOB->MODER &= 0xFFF5DDDD;
		GPIOB->MODER |= 0x00051111;
	
    /* configure PC13 for push button interrupt */
    GPIOC->MODER &= 0xF3FFFFFF;        /* set port C to input mode */
    
    SYSCFG->EXTICR[3] &= 0xFF0F;       /* clear port selection for EXTI13 */
    SYSCFG->EXTICR[3] |= 0x0020;        /* select port C for EXTI13 */
    
    EXTI->IMR |= 0x2000;                /* unmask EXTI13 */
    EXTI->FTSR |= 0x2000;               /* select falling edge trigger */

/*   NVIC->ISER[1] = 0x00000100;     */    /* enable IRQ40 (bit 8 of ISER[1]) */
    NVIC_EnableIRQ(EXTI15_10_IRQn);
    
    __enable_irq();                     /* global enable IRQs */
    
		
		while(1) {
			GPIOB->ODR &=0xFCFA;
			GPIOB->ODR |=0x0050;
				delayMs(3000);

			GPIOB->ODR &=0xFCEE;
			GPIOB->ODR |=0x0044;
				delayMs(1000);
							
/********************************************************************************/
/* Add interrup here*/	
				if(pressed == 1){
					GPIOB->ODR &=0xFCEB;
			GPIOB->ODR |=0x0041;
					CountDown();
				}

				GPIOB->ODR &= 0xFEAB;
				GPIOB->ODR |=0x0201;
				delayMs(3000);

				GPIOB->ODR &= 0xFDAB;
				GPIOB->ODR |=0x0101;
				delayMs(1000);   
/*******************************************************************************/
/*  Add interrupt*/
				if(pressed == 1){
					GPIOB->ODR &=0xFCEB;
			GPIOB->ODR |=0x0041;
					CountDown();
				}
    }
}

void CountDown(void)
{
	int something[] = {0x000, 0x3f0, 0x000, 0x3f0, 0x000, 0x3f0, 0x060, 0x5b0, 0x4f0, 0x660, 0x6d0, 0x7d0, 0x070, 0x7f0, 0x6f0}; 
	int i;
	
	for(i = 14; i>=0; i--) 
			{
				GPIOA->ODR = something[i];           
				delayMs(500);
			}		 
		
		EXTI->PR = 0x2000;  /* reset PR */
			pressed = 0;
}

/* Interrupt function */
void EXTI15_10_IRQHandler(void) {
	pressed = 1;
		EXTI->PR = 0x2000;  /* reset PR */	
}

/* 16 MHz SYSCLK */
void delayMs(int n) {
    int i;
    for (; n > 0; n--)
        for (i = 0; i < 1598; i++) ;
}
