// push constant 111
@111
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 333
@333
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 888
@888
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop static 8
@SP
M=M-1
@SP
A=M
A=M
D=A
@StaticTest.8
M=D
// pop static 3
@SP
M=M-1
@SP
A=M
A=M
D=A
@StaticTest.3
M=D
// pop static 1
@SP
M=M-1
@SP
A=M
A=M
D=A
@StaticTest.1
M=D
// push static 3
@StaticTest.3
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// push static 1
@StaticTest.1
A=M
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
// push static 8
@StaticTest.8
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
// program end loop
(VERY_END)
@VERY_END
0;JMP
