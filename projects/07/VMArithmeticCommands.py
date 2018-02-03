BINARY_COMMAND_TEMPLATE = '''// {command_name}
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
D={computation}
@SP
A=M
A=A-1
M=D
'''

UNARY_COMMAND_TEMPLATE = '''// {command_name}
@SP
A=M
A=A-1
A=M
D={computation}
@SP
A=M
A=A-1
M=D
'''

COMPARISON_COMMAND_TEMPLATE = '''// {command_name}
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
@IF_{comparison_type}_{counter}
D;{comparison_type}
@SP
A=M
A=A-1
M=-1
@END_{comparison_type}_{counter}
0;JMP
(IF_{comparison_type}_{counter})
@SP
A=M
A=A-1
M=0
(END_{comparison_type}_{counter})
'''

def _add(command_number):
	return BINARY_COMMAND_TEMPLATE.format(command_name='add', computation='A+D')


def _sub(command_number):
	return BINARY_COMMAND_TEMPLATE.format(command_name='sub', computation='A-D')


def _neg(command_number):
	return UNARY_COMMAND_TEMPLATE.format(command_name='neg', computation='-A')


def _eq(command_number):
	return COMPARISON_COMMAND_TEMPLATE.format(command_name='eq', comparison_type='JEQ', counter=command_number)


def _gt(command_number):
	return COMPARISON_COMMAND_TEMPLATE.format(command_name='gt', comparison_type='JGT', counter=command_number)


def _lt(command_number):
	return COMPARISON_COMMAND_TEMPLATE.format(command_name='lt', comparison_type='JLT', counter=command_number)


def _and(command_number):
	return BINARY_COMMAND_TEMPLATE.format(command_name='and', computation='D&A')


def _or(command_number):
	return BINARY_COMMAND_TEMPLATE.format(command_name='or', computation='A|D')


def _not(command_number):
	return UNARY_COMMAND_TEMPLATE.format(command_name='not', computation='!A')
