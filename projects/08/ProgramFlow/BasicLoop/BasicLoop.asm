// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 0
@SP
M=M-1
@SP
A=M
A=M
D=A
@LCL
A=M
M=D
// label LOOP_START
(LOOP_START)
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
// push local 0
@LCL
A=M
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
// pop local 0
@SP
M=M-1
@SP
A=M
A=M
D=A
@LCL
A=M
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
// if-goto LOOP_START
@SP
M=M-1
@SP
A=M
A=M
D=A
@LOOP_START
D;JNE
// push local 0
@LCL
A=M
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// program end loop
(VERY_END)
@VERY_END
0;JMP
