from VMCommon import FOLLOW_POINTER
from VMCommon import READ_AND_DECREMENT_SP

COMMENT = '// {command} {function_name}\n'

RETURN_ADDRESS = 'RET${class_name}${command_number}'

LABEL = '({address})\n'

PUSH_TO_STACK = '''@{value}
D=A
@SP
A=M
M=D
@SP
M=M+1
'''

GOTO_FUNCTION = '''@{function_name}
0;JMP
'''

READ = '''@{address}
A=M
D=A
'''

SUBTRACT = '''@{value}
D=D-A
'''

STORE = '''@{address}
M=D
'''


def call(class_name, command_number, function_name, argument_num):
	output = COMMENT.format(command='call', function_name=function_name)

	argument_num = int(argument_num)
	return_address = RETURN_ADDRESS.format(class_name=class_name, command_number=command_number)

	output += PUSH_TO_STACK.format(value=return_address)
	output += PUSH_TO_STACK.format(value='LCL')
	output += PUSH_TO_STACK.format(value='ARG')
	output += PUSH_TO_STACK.format(value='THIS')
	output += PUSH_TO_STACK.format(value='THAT')

	output += READ.format(address='SP')
	output += SUBTRACT.format(value=5)
	if argument_num > 0:
		output += SUBTRACT.format(value=argument_num)
	output += STORE.format(address='ARG')

	output += READ.format(address='SP')
	output += STORE.format(address='LCL')

	output += GOTO_FUNCTION.format(function_name=function_name)

	output += LABEL.format(address=return_address)

	return output


def function(class_name, command_number, function_name, local_variable_num):
	output = COMMENT.format(command='function', function_name=function_name)

	local_variable_num = int(local_variable_num)

	output += LABEL.format(address=function_name)

	for i in range(0, local_variable_num):
		output += PUSH_TO_STACK.format(value='0')

	return output


def ret(class_name, command_number):
	output = COMMENT.format(command='return', function_name='')

	output += READ.format(address='LCL')
	output += STORE.format(address='ENDFRAME')

	output += READ_AND_DECREMENT_SP
	output += '@ARG\n'
	output += 'A=M\n'
	output += 'M=D\n'

	output += READ.format(address='ARG')
	output += 'D=D+1\n'
	output += STORE.format(address='SP')

	output += READ.format(address='ENDFRAME')
	output += SUBTRACT.format(value=1)
	output += 'A=D\n'
	output += FOLLOW_POINTER
	output += 'D=A\n'
	output += STORE.format(address='THAT')

	output += READ.format(address='ENDFRAME')
	output += SUBTRACT.format(value=2)
	output += 'A=D\n'
	output += FOLLOW_POINTER
	output += 'D=A\n'
	output += STORE.format(address='THIS')

	output += READ.format(address='ENDFRAME')
	output += SUBTRACT.format(value=3)
	output += 'A=D\n'
	output += FOLLOW_POINTER
	output += 'D=A\n'
	output += STORE.format(address='ARG')

	output += READ.format(address='ENDFRAME')
	output += SUBTRACT.format(value=4)
	output += 'A=D\n'
	output += FOLLOW_POINTER
	output += 'D=A\n'
	output += STORE.format(address='LCL')

	output += READ.format(address='ENDFRAME')
	output += SUBTRACT.format(value=5)
	output += 'A=D\n'
	output += FOLLOW_POINTER
	output += 'D=A\n'
	output += '''A=D
0;JMP
'''

	return output

# endFrame = LCL
# retAddr = *(endFrame-5)
# *ARG = pop()
# SP=ARG+1
# THAT=*(endFrame-1)
# THIS=*(endFrame-2)
# ARG=*(endFrame-3)
# LCL=*(endFrame-4)
# goto retAddr