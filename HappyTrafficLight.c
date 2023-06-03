
#include "stm32f4xx.h"
#include "stdbool.h"

void CountDown(void);
void UrbanTrafficLight(void);
void RuralTrafficLight(void);
void EXTI15_10_IRQHandler(void);
void delayMs(int n);
void delayMs(int n);
void LCD_nibble_write(char data, unsigned char control);
void LCD_command(unsigned char command);
void LCD_data(char data);
void LCD_init(void);
void SysInit(void);
#define RS 0x20     /* PB5 mask for reg select */
#define EN 0x80     /* PB7 mask for enable */


struct State
{
	unsigned int output_mask0;
	unsigned int output_mask1;
  int delay; 
	char LCD_line1[6];
	char LCD_line2[4];
	bool countDown;  /* true: call countDown. false: do nothing */
	unsigned int *nextState[5];
};
typedef const struct State STyp;
#define S0 &FSM[0]
#define U1 &FSM[1]
#define U2 &FSM[2]
#define U3 &FSM[3]
#define U4 &FSM[4]
#define U5 &FSM[5]
#define U6 &FSM[6]
#define R1 &FSM[7]
#define R2 &FSM[8]
#define R3 &FSM[9]
#define R4 &FSM[10]

STyp FSM[11] = {
/* S0 */				{0xFFFF, 0x0355, 1000, {'*','*','*','*', '*', '*'}, {' ',' ',' ',' '}, false,{0, 0, 0, 0, 0}}, 
/* U1 */				{0xFEAB, 0x0201, 3000, {'U','R','B','A', 'N', '1'}, {' ',' ',' ',' '}, false, {S0, S0, U2, U2, 0}},
/* U2 */        {0xFDAB, 0x0101, 1000, {'U','R','B','A', 'N', '2'}, {' ',' ',' ',' '}, false, {U3, U5, U3, U5, 0}},
/* U3 */				{0xFCFA, 0x0050, 3000, {'U','R','B','A', 'N', '3'}, {' ',' ',' ',' '}, false,{S0, S0, U4, U4, 0}},
/* U4 */				{0xFCEE, 0x0044, 1000, {'U','R','B','A', 'N', '4'}, {' ',' ',' ',' '}, false,{U1, U6, U1, U6, 0}},
/* U5 */				{0xFCEB, 0x0041, 1000, {'U','R','B','A', 'N', '5'}, {'W','A','L','K'}, true, {U3, U3, U3, U3, 0}},
/* U6 */				{0xFCEB, 0x0041, 1000, {'U','R','B','A', 'N', '6'}, {'W','A','L','K'}, true, {U1, U1, U1, U1, 0}},
/* R1 */				{0xFEAB, 0x0201, 3000, {'R','U','R','A', 'L', '1'}, {' ',' ',' ',' '}, false, {R1, R1, R2, R2, S0}},
/* R2 */				{0xFDAB, 0x0101, 1000, {'R','U','R','A', 'L', '2'}, {' ',' ',' ',' '}, false, {R3, R3, R3, R3, R3}},
/* R3 */				{0xFCFA, 0x0050, 3000, {'R','U','R','A', 'L', '3'}, {' ', ' ', ' ', ' '}, false, {R3, R4, R3, R4, S0}},
/* R4 */				{0xFCEE, 0x0044, 1000, {'R','U','R','A', 'L', '4'}, {' ',' ',' ',' '}, false, {R1, R1, R1, R1, R1}}
};



int pressed = 0; /*added*/

int main(void) {
	
	/* initialize LCD controller */
  SysInit();  
	LCD_init();
	
	STyp *currentState;
		currentState = S0;
		
		
		while(1) {
			
			GPIOB->ODR &= currentState->output_mask0;
			GPIOB->ODR |= currentState->output_mask1;
			
			for(int i = 0; i < 6; i++)
			{
				LCD_data(currentState->LCD_line1[i]);
			}
			for(int k = 0; k < 35; k++)
			{
				LCD_data(' ');
			}
			for(int j = 0; j < 4; j++)
			{
				LCD_data(currentState->LCD_line2[j]);
			}
			delayMs(currentState->delay);
			
			if(currentState->countDown)
			{
				CountDown();
			}
			LCD_command(1);
			delayMs(5);
/*			currentState = currentState->nextState[(GPIOC->IDR) & 0x00000003];*/
/*			if(currentState == S0)  
			{
								
			}  */
			
			if(currentState == S0)
			{
				pressed = 0;
				if((GPIOC->IDR & 0x0004) == 4)
				{
					currentState = U1;
				}
				if((GPIOC->IDR & 0x0004) == 0)
				{
					currentState = R1;
				}
			}
			else if(currentState >= U1 && currentState <= U6)
			{
			
				int mode = (GPIOC->IDR & 0x0004)/2;
				currentState = currentState->nextState[mode+pressed];
			}
			else if(currentState >= R1 && currentState <= R4)
			{
				
				int input = GPIOC->IDR & 0x0007;
				if(input > 4)
				{
					input = 4;
				}
				currentState = currentState->nextState[input];
			}
			
		}
}

void SysInit(void){
		__disable_irq();                    /* global disable IRQs */
	  RCC->AHB1ENR |= 7; /* enable GPIOA & GPIOC clock */
    RCC->APB2ENR |= 0x4000;             /* enable SYSCFG clock */
    GPIOA->MODER &= 0xFF5555FD;        /* clear pin mode */
    GPIOA->MODER |= 0x00555501; 					/* set port A as Output */
		/* Comfig PB0,2,4,6,8,9 for output (Traffic lights). PB5 PB7 for LCD RS and EN */
		GPIOB->MODER &= 0xFFF555DD;
		GPIOB->MODER |= 0x00055511;
		/* PC4-PC7 for LCD D4-D7, respectively. PC13 for interrupt button. PC0 and PC1 for EW/NS sensors. PC2 for mode selection */
    GPIOC->MODER &= 0xF3FF55C0;    /* clear pin mode */
    GPIOC->MODER |= 0x00005500;    /* set pin output mode */
    GPIOB->BSRR = 0x00800000;       /* turn off EN */
    SYSCFG->EXTICR[3] &= 0xFF0F;       /* clear port selection for EXTI13 */
    SYSCFG->EXTICR[3] |= 0x0020;        /* select port C for EXTI13 */
    EXTI->IMR |= 0x2000;                /* unmask EXTI13 */
    EXTI->FTSR |= 0x2000;               /* select falling edge trigger */
/*   NVIC->ISER[1] = 0x00000100;     */    /* enable IRQ40 (bit 8 of ISER[1]) */
    NVIC_EnableIRQ(EXTI15_10_IRQn);
    __enable_irq();  /* global enable IRQs */                  
}

void CountDown(void)
{
	int sevenSeg[] = {0x001, 0x3f1, 0x001, 0x3f0, 0x000, 0x3f1, 0x060, 0x5b0, 0x4f1, 0x660, 0x6d0, 0x7d1, 0x070, 0x7f0, 0x6f1}; 
	int i;
	for(i = 14; i>=0; i--) 
			{
				GPIOA->ODR = sevenSeg[i];           
				delayMs(500);
			}	
  		GPIOA->ODR &= 0xFFFE;	
			pressed = 0;
}

/* Interrupt function */
void EXTI15_10_IRQHandler(void) {
	pressed = 1;
/*	GPIOA->ODR |= 0x00000001;
	delayMs(300);  */
/*	CountDown(); */
	EXTI->PR = 0x2000;  /* reset PR */	
/*	GPIOA->ODR &= 0xFFFE;*/
}

/* initialize GPIOB/C then initialize LCD controller */
void LCD_init(void) {

    delayMs(20);                /* LCD controller reset sequence */
    LCD_nibble_write(0x30, 0);
    delayMs(5);
    LCD_nibble_write(0x30, 0);
    delayMs(1);
    LCD_nibble_write(0x30, 0);
    delayMs(1);

    LCD_nibble_write(0x20, 0);  /* use 4-bit data mode */
    delayMs(1);
    LCD_command(0x28);          /* set 4-bit data, 2-line, 5x7 font */
    LCD_command(0x06);          /* move cursor right */
    LCD_command(0x01);          /* clear screen, move cursor to home */
    LCD_command(0x0F);          /* turn on display, cursor blinking */
}

void LCD_nibble_write(char data, unsigned char control) {
    /* populate data bits */
    GPIOC->BSRR = 0x00F00000;       /* clear data bits */
    GPIOC->BSRR = data & 0xF0;      /* set data bits */

    /* set R/S bit */
    if (control & RS)
        GPIOB->BSRR = RS;
    else
        GPIOB->BSRR = RS << 16;

    /* pulse E */
    GPIOB->BSRR = EN;
    delayMs(0);
    GPIOB->BSRR = EN << 16;
}

void LCD_command(unsigned char command) {
    LCD_nibble_write(command & 0xF0, 0);    /* upper nibble first */
    LCD_nibble_write(command << 4, 0);      /* then lower nibble */

    if (command < 4)
        delayMs(2);         /* command 1 and 2 needs up to 1.64ms */
    else
        delayMs(1);         /* all others 40 us */
}

void LCD_data(char data) {
    LCD_nibble_write(data & 0xF0, RS);      /* upper nibble first */
    LCD_nibble_write(data << 4, RS);        /* then lower nibble */

    delayMs(2);
}

/* delay n milliseconds (16 MHz CPU clock) */
void delayMs(int n) {
	int i;
	SysTick->LOAD = 16000;
	SysTick->VAL = 0;
	SysTick->CTRL = 0x5;
	for(i = 0; i < n; i++){
		while((SysTick->CTRL & 0x10000) == 0) 
		{}
	}
	SysTick -> CTRL = 0;
}
