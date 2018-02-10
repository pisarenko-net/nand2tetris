from VMCommon import ADDRESS
from VMCommon import FOLLOW_POINTER
from VMCommon import LOAD_VALUE_TO_REGISTER
from VMCommon import READ_AND_DECREMENT_SP
from VMCommon import STORE_VALUE_FROM_REGISTER
from VMCommon import WRITE_AND_INCREMENT_SP
from VMCommon import WRITE_TO_MEMORY_FROM_REGISTER


RETURN_ADDRESS = 'RETURN_ADDRESS'

OFFSET_ENDFRAME = {
	'THAT': 1,
	'THIS': 2,
	'ARG': 3,
	'LCL': 4,
	RETURN_ADDRESS: 5
}

COMMENT = '// {command} {function_name} {argument_num}\n'

RETURN_ADDRESS_LABEL = 'RET${class_name}${command_number}'

LABEL = '({address})\n'

JUMP = '0;JMP\n'

SUBTRACT = '''@{value}
D=D-A
'''

GOTO = ADDRESS + JUMP

READ = ADDRESS + FOLLOW_POINTER + LOAD_VALUE_TO_REGISTER

STORE = ADDRESS + WRITE_TO_MEMORY_FROM_REGISTER


def bootstrap():
	output = COMMENT.format(command='bootstrap', function_name='', argument_num='')
	output += ADDRESS.format(address='256')
	output += LOAD_VALUE_TO_REGISTER
	output += STORE.format(address='SP')
	output += call('bootstrap', 0, 'Sys.init', 0)
	return output


def call(class_name, command_number, function_name, argument_num):
	output = COMMENT.format(command='call', function_name=function_name, argument_num=argument_num)

	argument_num = int(argument_num)
	return_address = RETURN_ADDRESS_LABEL.format(class_name=class_name, command_number=command_number)

	output += ADDRESS.format(address=return_address)
	output += LOAD_VALUE_TO_REGISTER
	output += WRITE_AND_INCREMENT_SP

	for address in ['LCL', 'ARG', 'THIS', 'THAT']:
		output += ADDRESS.format(address=address)
		output += FOLLOW_POINTER
		output += LOAD_VALUE_TO_REGISTER
		output += WRITE_AND_INCREMENT_SP

	output += READ.format(address='SP')
	output += SUBTRACT.format(value=5)
	if argument_num > 0:
		output += SUBTRACT.format(value=argument_num)
	output += STORE.format(address='ARG')

	output += READ.format(address='SP')
	output += STORE.format(address='LCL')

	output += GOTO.format(address=function_name)

	output += LABEL.format(address=return_address)

	return output


def function(class_name, command_number, function_name, local_variable_num):
	output = COMMENT.format(command='function', function_name=function_name, argument_num=local_variable_num)

	local_variable_num = int(local_variable_num)

	output += LABEL.format(address=function_name)

	for i in range(0, local_variable_num):
		output += ADDRESS.format(address='0')
		output += LOAD_VALUE_TO_REGISTER
		output += WRITE_AND_INCREMENT_SP

	return output


def ret(class_name, command_number):
	output = COMMENT.format(command='return', function_name='', argument_num='')

	output += READ.format(address='LCL')
	output += STORE.format(address='ENDFRAME')

	output += _set_address_from_endframe(RETURN_ADDRESS, OFFSET_ENDFRAME[RETURN_ADDRESS])

	output += READ_AND_DECREMENT_SP
	output += ADDRESS.format(address='ARG')
	output += FOLLOW_POINTER
	output += WRITE_TO_MEMORY_FROM_REGISTER

	output += READ.format(address='ARG')
	output += 'D=D+1\n'
	output += STORE.format(address='SP')

	for address in ['THAT', 'THIS', 'ARG', 'LCL']:
		output += _set_address_from_endframe(address, OFFSET_ENDFRAME[address])

	output += ADDRESS.format(address=RETURN_ADDRESS)
	output += FOLLOW_POINTER
	output += JUMP

	return output


def _set_address_from_endframe(address, offset_endframe):
	output = READ.format(address='ENDFRAME')
	output += SUBTRACT.format(value=offset_endframe)
	output += STORE_VALUE_FROM_REGISTER
	output += FOLLOW_POINTER
	output += LOAD_VALUE_TO_REGISTER
	output += STORE.format(address=address)
	return output
