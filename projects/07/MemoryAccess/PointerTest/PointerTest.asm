// push constant 3030
@3030
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
// push constant 3040
@3040
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
// push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop this 2
@SP
M=M-1
@SP
A=M
A=M
D=A
@THIS
A=M
A=A+1
A=A+1
M=D
// push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that 6
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
A=A+1
A=A+1
A=A+1
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
// push this 2
@THIS
A=M
A=A+1
A=A+1
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
// push that 6
@THAT
A=M
A=A+1
A=A+1
A=A+1
A=A+1
A=A+1
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
