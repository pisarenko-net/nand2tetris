from VMCommon import WRITE_AND_INCREMENT_SP
from VMCommon import READ_AND_DECREMENT_SP
from VMCommon import COPY_FROM_A_TO_D
from VMCommon import WRITE_TO_MEMORY_FROM_REGISTER
from VMCommon import FOLLOW_POINTER


MEMORY_SEGMENT_ADDRESSES = {
	'local': 'LCL',
	'argument': 'ARG',
	'this': 'THIS',
	'that': 'THAT'
}

TEMP_BASE_ADDRESS = 5

ADDRESS_TEMPLATE = '@{address}\n'

COMMENT_TEMPLATE = '// {command} {memory_segment_name} {value}\n'


def push(class_name, command_number, memory_segment, value):
	address_offset = int(value)

	output = COMMENT_TEMPLATE.format(command='push', memory_segment_name=memory_segment, value=value)
	output += ADDRESS_TEMPLATE.format(address=_get_base_address(class_name, memory_segment, address_offset))

	if memory_segment == 'constant':
		output += COPY_FROM_A_TO_D
	elif memory_segment == 'static':
		output += FOLLOW_POINTER
		output += COPY_FROM_A_TO_D
	else:
		if memory_segment in MEMORY_SEGMENT_ADDRESSES:
			output += FOLLOW_POINTER

		if address_offset != 0:
			output += _increment_memory(address_offset)

		output += FOLLOW_POINTER
		output += COPY_FROM_A_TO_D

	output += WRITE_AND_INCREMENT_SP
	return output


def pop(class_name, command_number, memory_segment, value):
	address_offset = int(value)

	output = COMMENT_TEMPLATE.format(command='pop', memory_segment_name=memory_segment, value=address_offset)
	output += READ_AND_DECREMENT_SP
	output += ADDRESS_TEMPLATE.format(address=_get_base_address(class_name, memory_segment, address_offset))

	if memory_segment == 'static':
		output += WRITE_TO_MEMORY_FROM_REGISTER
	else:
		if memory_segment == 'pointer':
			output += WRITE_TO_MEMORY_FROM_REGISTER
		elif memory_segment in MEMORY_SEGMENT_ADDRESSES:
			output += FOLLOW_POINTER

		if address_offset != 0:
			output += _increment_memory(address_offset)

		output += WRITE_TO_MEMORY_FROM_REGISTER
	return output


def _increment_memory(times):
	return '\n'.join(['A=A+1'] * times) + '\n'


def _get_base_address(class_name, memory_segment, address_offset):
	if memory_segment == 'temp':
		return TEMP_BASE_ADDRESS
	elif memory_segment == 'constant':
		return address_offset
	elif memory_segment == 'static':
		return '{class_name}.{address_reference}'.format(class_name=class_name, address_reference=address_offset)
	elif memory_segment == 'pointer':
		return _compute_pointer_address(address_offset)
	else:
		return MEMORY_SEGMENT_ADDRESSES[memory_segment]


def _compute_pointer_address(address_offset):
	return 'THIS' if address_offset == 0 else 'THAT'
