// push argument 1
@ARG
A=M
A=A+1
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 1
@SP
M=M-1
@SP
A=M
A=M
D=A
@THAT
M=D
A=A+1
M=D
// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 0
@SP
M=M-1
@SP
A=M
A=M
D=A
@THAT
A=M
M=D
// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 1
@SP
M=M-1
@SP
A=M
A=M
D=A
@THAT
A=M
A=A+1
M=D
// push argument 0
@ARG
A=M
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
A=M
A=A-1
A=M
D=A
@SP
M=M-1
A=M
A=A-1
A=M
D=A-D
@SP
A=M
A=A-1
M=D
// pop argument 0
@SP
M=M-1
@SP
A=M
A=M
D=A
@ARG
A=M
M=D
// label MAIN_LOOP_START 
(MAIN_LOOP_START)
// push argument 0
@ARG
A=M
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// if-goto COMPUTE_ELEMENT 
@SP
M=M-1
@SP
A=M
A=M
D=A
@COMPUTE_ELEMENT
D;JNE
// goto END_PROGRAM 
@END_PROGRAM
0;JMP
// label COMPUTE_ELEMENT 
(COMPUTE_ELEMENT)
// push that 0
@THAT
A=M
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// push that 1
@THAT
A=M
A=A+1
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
A=M
A=A-1
A=M
D=A
@SP
M=M-1
A=M
A=A-1
A=M
D=A+D
@SP
A=M
A=A-1
M=D
// pop that 2
@SP
M=M-1
@SP
A=M
A=M
D=A
@THAT
A=M
A=A+1
A=A+1
M=D
// push pointer 1
@THAT
A=A+1
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
A=M
A=A-1
A=M
D=A
@SP
M=M-1
A=M
A=A-1
A=M
D=A+D
@SP
A=M
A=A-1
M=D
// pop pointer 1
@SP
M=M-1
@SP
A=M
A=M
D=A
@THAT
M=D
A=A+1
M=D
// push argument 0
@ARG
A=M
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
A=M
A=A-1
A=M
D=A
@SP
M=M-1
A=M
A=A-1
A=M
D=A-D
@SP
A=M
A=A-1
M=D
// pop argument 0
@SP
M=M-1
@SP
A=M
A=M
D=A
@ARG
A=M
M=D
// goto MAIN_LOOP_START 
@MAIN_LOOP_START
0;JMP
// label END_PROGRAM 
(END_PROGRAM)
