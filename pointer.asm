// push constant 9
@9
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 23
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer 0
@SP
M=M-1
@SP
A=M
A=M
D=A
@THIS
M=D
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
// push pointer 0
@THIS
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// push pointer 0
@THIS
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
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
// program end loop
(VERY_END)
@VERY_END
0;JMP
