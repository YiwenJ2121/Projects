#include "stm32f4xx.h"

void delayMs(int n);

int main(void) {
    RCC->AHB1ENR |= 6; /*********************************** B-output    C-input*/

		/* Comfig PB0,2,4,6,8,9 for output (Traffic lights) */
		GPIOB->MODER &= 0xFFF5DDDD;
		GPIOB->MODER |= 0x00051111;
    GPIOC->MODER &= 0xFFFFFFF0;   /************************ C0 C1 input*/
		struct State
		{
			unsigned int outputs_mask0;
			unsigned int outputs_mask1;
			int delay;   /* in ms  */
			unsigned int nextState[4];   /* index of nextState is GPIOC->IDR &= 0x00000003 */
		};
	
		typedef const struct State STyp;
		#define S0 0
		#define S1 1
		#define S2 2
		#define S3 3
		
		STyp FSM[4] = {
			{0xFCFA, 0x0050,3000,{S0,S0,S1,S1}}, 
			{0xFCEE, 0x0044, 500,{S2,S2,S2,S2}},
			{0xFEAB, 0x0201,3000,{S2,S3,S2,S3}},
			{0xFDAB, 0x0101, 500,{S0,S0,S0,S0}}
		};

		unsigned int currentState = S0;
		while(1) {
			GPIOB->ODR &= FSM[currentState].outputs_mask0;
			GPIOB->ODR |= FSM[currentState].outputs_mask1;
			delayMs(FSM[currentState].delay);

			currentState = FSM[currentState].nextState[((GPIOC->IDR) & 0x00000003)];
		}
}

/* 16 MHz SYSCLK */
void delayMs(int n) {
    int i;
    for (; n > 0; n--)
        for (i = 0; i < 1598; i++) ;
}
