@1  // push constant 7
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP // not
A=M
A=A-1
A=M
D=!A
@SP
A=M
A=A-1
M=D

@8  // push constant 8
D=A
@SP
A=M
M=D
@SP
M=M+1

@SP // add
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

@SP // neg
A=M
A=A-1
A=M
D=-A
@SP
A=M
A=A-1
M=D