// push temp 2
@5
A=A+1
A=A+1
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop temp 3
@SP
M=M-1
@SP
A=M
A=M
D=A
@5
A=M
A=A+1
A=A+1
A=A+1
M=D
// program end loop
(VERY_END)
@VERY_END
0;JMP
