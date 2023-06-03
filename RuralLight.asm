; Assembly program using Assembly to toggle Urban light(LD2 -> PA5) Using ODR
; on STM32F446RE Nucleo64 board at 1 Hz
;
			EXPORT __Vectors
			EXPORT Reset_Handler
			AREA vectors, CODE, READONLY
__Vectors 	DCD 0x10010000 ; 0x20008000 ; Top of Stack
			DCD Reset_Handler ; Reset Handler
RCC_AHB1ENR equ 0x40023830    ; GPIO AHB1 clock enable address
GPIOC_MODER equ 0x40020800    ; port C moder address
GPIOA_MODER equ 0x40020000    ; port A moder address
GPIOC_ODR   equ 0x40020814    ; port C ODR address
GPIOA_IDR   equ 0x40020010    ; port A IDR address
GPIOA_PUPDR equ 0x4002000C    ; port A PUPDR address

			AREA PROG, CODE, READONLY
Reset_Handler
			ldr r4, =RCC_AHB1ENR 
			ldr r6, [r4]
            orr r5, r6, #5            
			str r5, [r4]                ; enable GPIOA and C clock
			ldr r4, =GPIOC_MODER
			ldr r5, =0x00000555 
			str r5, [r4]                ; set C0-C5 output
			ldr r4, =GPIOA_MODER
			ldr r5, [r4]
			and r5, r5, #0xFFFFFF00
			str r5, [r4]                ; set A0 A1 input
			ldr r4, =GPIOA_PUPDR
			ldr r5, =0x5
			str r5, [r4]                ; set A PUPDR Vcc

L1 			ldr r4, =GPIOC_ODR          ; NS-g, EW-r
			mov r5, #0x21 
			str r5, [r4]
			ldr r0, =3000
			bl delay
			
EW_noCar	ldr r4, = GPIOA_IDR         ; Check the traffic in EW
			ldr r5, [r4]
			and r5, r5, #0x00000001
			cmp r5, #1
			beq EW_noCar

			ldr r4, =GPIOC_ODR          ; NS-y, EW-r
			mov r5, #0x22 ;
			str r5, [r4]
			ldr r0, =1000
			bl delay

			ldr r4, =GPIOC_ODR          ; NS-r,EW-g
			mov r5, #0x0C ;
			str r5, [r4]
			ldr r0, =3000
			bl delay

NS_noCar	ldr r4, = GPIOA_IDR         ; Check the traffic in NS
			ldr r5, [r4]
			and r5, r5, #0x00000002
			cmp r5, #2
			beq NS_noCar

			ldr r4, =GPIOC_ODR          ; NS-r,EW-y
			mov r5, #0x14 ;
			str r5, [r4]
			ldr r0, =1000
			bl delay
			b L1 ; 

; delay milliseconds in R0
delay 	    ldr r1, =5325
DL1 		subs r1, r1, #1
			bne DL1
			subs r0, r0, #1
			bne delay
			bx lr
			end