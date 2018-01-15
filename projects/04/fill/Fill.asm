// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

	// initialize the wanted and current colors
	@current_color
	M=0
	@wanted_color
	M=0

	// compute end address of the screen
	@SCREEN
	D=A
	@8192
	D=D+A
	@end_screen_address
	M=D

(LOOP_KEYBOARD_CHECK)
	// wanted_color = current_color
	@wanted_color
	D=M
	@current_color
	M=D

	@KBD
	D=M
	@SET_WANTED_COLOR_WHITE
	D;JEQ

(SET_WANTED_COLOR_BLACK)
	// set wanted color to black
	@wanted_color
	M=-1
	// if current_color == wanted_color, go to LOOP_KEYBOARD_CHECK
	D=M
	@current_color
	D=D-M
	@LOOP_KEYBOARD_CHECK
	D;JEQ
	// screen repaint is necessary
	@SCREEN_PAINT
	0;JMP

(SET_WANTED_COLOR_WHITE)
	// set wanted color to white
	@wanted_color
	M=0
	// if current_color == wanted_color, go to LOOP_KEYBOARD_CHECK
	D=M
	@current_color
	D=D-M
	@LOOP_KEYBOARD_CHECK
	D;JEQ
	// screen repaint is necessary

(SCREEN_PAINT)
	// initialize screen paint counter
	@SCREEN
	D=A
	@curr_screen_address
	M=D

(LOOP_SCREEN_PAINT)
	// if curr_screen_address == end_screen_address
	@curr_screen_address
	D=M
	@end_screen_address
	D=M-D
	@LOOP_KEYBOARD_CHECK
	D;JEQ

    // paint one word at a time
	@wanted_color
	D=M
	@curr_screen_address
	A=M
	M=D

	// curr_screen_address += word
	@curr_screen_address
	D=M
	D=D+1
	M=D

	@LOOP_SCREEN_PAINT
	0;JMP
