@LCL
A=M
D=A
@ENDFRAME
M=D
@SP
M=M-1
@SP
A=M
A=M
D=A
@ARG
M=D
D=D+1
@SP
M=D
@ENDFRAME
A=M
D=A
D=D-1
@THAT
M=D
D=D-1
@THIS
M=D
D=D-1
@ARG
M=D
D=D-1
@LCL
M=D
D=D-1
@RETURN_ADDRESS
A=D
0;JMP




// endFrame = LCL
// retAddr = *(endFrame-5)
// *ARG = pop()
// SP=ARG+1
// THAT=*(endFrame-1)
// THIS=*(endFrame-2)
// ARG=*(endFrame-3)
// LCL=*(endFrame-4)
// goto retAddr
