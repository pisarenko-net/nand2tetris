// push static 0
@Foo.0
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop static 2
@SP
M=M-1
@SP
A=M
A=M
D=A
@Foo.2
M=D