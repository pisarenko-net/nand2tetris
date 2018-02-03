@7  // push constant 7
D=A
@SP
A=M
M=D
@SP
M=M+1

@8  // push constant 8
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP // eq
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
@IF_1
D;JGT
@SP
A=M
A=A-1
M=-1
@END
0;JMP
(IF_1)
@SP
A=M
A=A-1
M=0
(END)

