// bootstrap  
@256
D=A
@SP
M=D
// call Sys.init 0
@RET$bootstrap$0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
D=A
@5
D=D-A
@ARG
M=D
@SP
A=M
D=A
@LCL
M=D
@Sys.init
0;JMP
(RET$bootstrap$0)
// function Sys.init 0
(Sys.init)
// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1
@RET$Sys$3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
D=A
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
A=M
D=A
@LCL
M=D
@Main.fibonacci
0;JMP
(RET$Sys$3)
// label WHILE
(WHILE)
// goto WHILE
@WHILE
0;JMP
// function Main.fibonacci 0
(Main.fibonacci)
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
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
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
@IF_JLT_9
D;JLT
@SP
A=M
A=A-1
M=0
@END_JLT_9
0;JMP
(IF_JLT_9)
@SP
A=M
A=A-1
M=-1
(END_JLT_9)
// if-goto IF_TRUE
@SP
M=M-1
@SP
A=M
A=M
D=A
@IF_TRUE
D;JNE
// goto IF_FALSE
@IF_FALSE
0;JMP
// label IF_TRUE
(IF_TRUE)
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
// return  
@LCL
A=M
D=A
@ENDFRAME
M=D
@ENDFRAME
A=M
D=A
@5
D=D-A
A=D
A=M
D=A
@RETURN_ADDRESS
M=D
@SP
M=M-1
@SP
A=M
A=M
D=A
@ARG
A=M
M=D
@ARG
A=M
D=A
D=D+1
@SP
M=D
@ENDFRAME
A=M
D=A
@1
D=D-A
A=D
A=M
D=A
@THAT
M=D
@ENDFRAME
A=M
D=A
@2
D=D-A
A=D
A=M
D=A
@THIS
M=D
@ENDFRAME
A=M
D=A
@3
D=D-A
A=D
A=M
D=A
@ARG
M=D
@ENDFRAME
A=M
D=A
@4
D=D-A
A=D
A=M
D=A
@LCL
M=D
@RETURN_ADDRESS
A=M
0;JMP
// label IF_FALSE
(IF_FALSE)
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
// push constant 2
@2
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
// call Main.fibonacci 1
@RET$Main$19
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
D=A
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
A=M
D=A
@LCL
M=D
@Main.fibonacci
0;JMP
(RET$Main$19)
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
// call Main.fibonacci 1
@RET$Main$23
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
@SP
A=M
D=A
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
A=M
D=A
@LCL
M=D
@Main.fibonacci
0;JMP
(RET$Main$23)
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
// return  
@LCL
A=M
D=A
@ENDFRAME
M=D
@ENDFRAME
A=M
D=A
@5
D=D-A
A=D
A=M
D=A
@RETURN_ADDRESS
M=D
@SP
M=M-1
@SP
A=M
A=M
D=A
@ARG
A=M
M=D
@ARG
A=M
D=A
D=D+1
@SP
M=D
@ENDFRAME
A=M
D=A
@1
D=D-A
A=D
A=M
D=A
@THAT
M=D
@ENDFRAME
A=M
D=A
@2
D=D-A
A=D
A=M
D=A
@THIS
M=D
@ENDFRAME
A=M
D=A
@3
D=D-A
A=D
A=M
D=A
@ARG
M=D
@ENDFRAME
A=M
D=A
@4
D=D-A
A=D
A=M
D=A
@LCL
M=D
@RETURN_ADDRESS
A=M
0;JMP
