// function Sys.init
(Sys.init)
// push constant 4000
@4000
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
// push constant 5000
@5000
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
// call Sys.main
@RET$Sys$5
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT
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
@Sys.main
0;JMP
(RET$Sys$5)
// pop temp 1
@SP
M=M-1
@SP
A=M
A=M
D=A
@5
A=A+1
M=D
// label LOOP
(LOOP)
// goto LOOP
@LOOP
0;JMP
// function Sys.main
(Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant 4001
@4001
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
// push constant 5001
@5001
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
// push constant 200
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 1
@SP
M=M-1
@SP
A=M
A=M
D=A
@LCL
A=M
A=A+1
M=D
// push constant 40
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 2
@SP
M=M-1
@SP
A=M
A=M
D=A
@LCL
A=M
A=A+1
A=A+1
M=D
// push constant 6
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 3
@SP
M=M-1
@SP
A=M
A=M
D=A
@LCL
A=M
A=A+1
A=A+1
A=A+1
M=D
// push constant 123
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Sys.add12
@RET$Sys$21
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=A
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=A
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=A
@SP
A=M
M=D
@SP
M=M+1
@THAT
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
@Sys.add12
0;JMP
(RET$Sys$21)
// pop temp 0
@SP
M=M-1
@SP
A=M
A=M
D=A
@5
M=D
// push local 0
@LCL
A=M
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// push local 1
@LCL
A=M
A=A+1
A=M
D=A
@SP
A=M
M=D
@SP
M=M+1
// push local 2
@LCL
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
// push local 3
@LCL
A=M
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
// push local 4
@LCL
A=M
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
@ENDFRAME
A=M
D=A
@5
D=D-A
A=D
A=M
D=A
A=D
0;JMP
// function Sys.add12
(Sys.add12)
// push constant 4002
@4002
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
// push constant 5002
@5002
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
// push constant 12
@12
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
// return 
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
@ENDFRAME
A=M
D=A
@5
D=D-A
A=D
A=M
D=A
A=D
0;JMP
