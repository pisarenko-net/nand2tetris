MEMORY_SEGMENT_ADDRESSES = {
	'local': 'LCL',
	'argument': 'ARG',
	'this': 'THIS',
	'that': 'THAT'
}

TEMP_BASE_ADDRESS = 5

ADDRESS_TEMPLATE = '@{address}\n'

PUSH_COMMENT = '// push {memory_segment_name} {value}\n'

WRITE_AND_INCREMENT_SP = '''@SP
A=M
M=D
@SP
M=M+1
'''

PUSH_CONSTANT_TEMPLATE = 'D=A\n'

PUSH_STATIC_TEMPLATE = '''A=M
D=A
'''

PUSH_START_TEMPLATE = 'A=M\n'

PUSH_END_TEMPLATE = '''A=M
D=A
'''

POP_COMMENT = '// pop {memory_segment_name} {address_offset}\n'

READ_AND_DECREMENT_SP = '''@SP
M=M-1
@SP
A=M
A=M
D=A
'''

POP_STATIC_TEMPLATE = 'M=D\n'

POP_START_TEMPLATE = 'A=M\n'

POP_POINTER_START_TEMPLATE = 'M=D\n'

POP_END_TEMPLATE = 'M=D\n'


def push(class_name, command_number, memory_segment, value):
	address_offset = int(value)

	output = PUSH_COMMENT.format(memory_segment_name=memory_segment, value=value)
	output += ADDRESS_TEMPLATE.format(address=_get_base_address(class_name, memory_segment, address_offset))

	if memory_segment == 'constant':
		output += PUSH_CONSTANT_TEMPLATE
	elif memory_segment == 'static':
		output += PUSH_STATIC_TEMPLATE
	else:
		if memory_segment == 'temp' or memory_segment == 'pointer':
			pass
		else:
			output += PUSH_START_TEMPLATE

		if address_offset != 0:
			output += _increment_memory(address_offset)

		output += PUSH_END_TEMPLATE

	output += WRITE_AND_INCREMENT_SP
	return output


def pop(class_name, command_number, memory_segment, value):
	address_offset = int(value)

	output = POP_COMMENT.format(memory_segment_name=memory_segment, address_offset=address_offset)
	output += READ_AND_DECREMENT_SP
	output += ADDRESS_TEMPLATE.format(address=_get_base_address(class_name, memory_segment, address_offset))

	if memory_segment == 'static':
		output += POP_STATIC_TEMPLATE
	else:
		if memory_segment == 'temp':
			pass
		elif memory_segment == 'pointer':
			output += POP_POINTER_START_TEMPLATE
		else:
			output += POP_START_TEMPLATE

		if address_offset != 0:
			output += _increment_memory(address_offset)

		output += POP_END_TEMPLATE
	return output


def _increment_memory(times):
	return '\n'.join(['A=A+1'] * times) + '\n'


def _get_base_address(class_name, memory_segment, address_offset):
	if memory_segment == 'temp':
		return TEMP_BASE_ADDRESS
	elif memory_segment == 'constant':
		return address_offset
	elif memory_segment == 'static':
		return '{class_name}.{address_reference}'.format(class_name=class_name, address_reference=value)
	elif memory_segment == 'pointer':
		return _compute_pointer_address(address_offset)
	else:
		return MEMORY_SEGMENT_ADDRESSES[memory_segment]


def _compute_pointer_address(address_offset):
	return 'THIS' if address_offset == 0 else 'THAT'
