ADDRESS = '@{address}\n'

LABEL = '({address})\n'

COMMENT = '// {command} {name} {arg}\n'

WRITE_AND_INCREMENT_SP = '''@SP
A=M
M=D
@SP
M=M+1
'''

READ_AND_DECREMENT_SP = '''@SP
M=M-1
@SP
A=M
A=M
D=A
'''

LOAD_VALUE_TO_REGISTER = 'D=A\n'

STORE_VALUE_FROM_REGISTER = 'A=D\n'

WRITE_TO_MEMORY_FROM_REGISTER = 'M=D\n'

FOLLOW_POINTER = 'A=M\n'

JUMP = '0;JMP\n'

GOTO = ADDRESS + JUMP