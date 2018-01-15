// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.
	@n
	M=0
	@R2
	M=0

(LOOP)
	@n
	D=M

	@R0    // if n=R1, end loop
	D=D-M
	@END
	D;JEQ

	@n
	D=M
	M=D+1  // n++

	@R1
	D=M
	@R2
	M=M+D  // R2 += R2

	@LOOP
	0;JMP  // continue looping

(END)
    @END
	0;JMP