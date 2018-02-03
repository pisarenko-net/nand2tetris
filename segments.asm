// push constant 17
@17
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
// pop LCL 0
@SP
M=M-1
@SP
A=M
A=M
D=A
@LCL
A=M
M=D
// pop static 3
@SP
M=M-1
@SP
A=M
A=M
D=A
@segments.3
M=D
// program end loop
(VERY_END)
@VERY_END
0;JMP
