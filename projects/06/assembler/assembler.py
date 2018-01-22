import re
import sys


INPUT_FILENAME = sys.argv[1]

COMMENT_REGEX = re.compile(r'(//.*)')
LABEL_REGEX = re.compile(r'^\s*\((.*)\)\s*$')
INSTRUCTION_A_REGEX = re.compile(r'^@(.*)$')
INSTRUCTION_C_DEST_REGEX = re.compile(r'(.*)=')
INSTRUCTION_C_COMP_REGEX = re.compile(r'(.*=)+(.*)(;.*)+')
INSTRUCTION_C_JUMP_REGEX = re.compile(r';(.*)')

JUMP_MAP = {
	'JGT': '001',
	'JEQ': '010',
	'JGE': '011',
	'JLT': '100',
	'JNE': '101',
	'JLE': '110',
	'JMP': '111'
}

DESTINATION_MAP = {
	'M':   '001',
	'D':   '010',
	'MD':  '011',
	'A':   '100',
	'AM':  '101',
	'AD':  '110',
	'AMD': '111'
}

COMP_MAP = {
	'0'  : '0101010',
	'1'  : '0111111',
	'-1' : '0111010',
	'D'  : '0001100',
	'A'  : '0110000',
	'!D' : '0001101',
	'!A' : '0110001',
	'-D' : '0001111',
	'-A' : '0110011',
	'D+1': '0011111',
	'A+1': '0110111',
	'D-1': '0001110',
	'A-1': '0110010',
	'D+A': '0000010',
	'D-A': '0010011',
	'A-D': '0000111',
	'D&A': '0000000',
	'D|A': '0010101',
	'M'  : '1110000',
	'!M' : '1110001',
	'-M' : '1110011',
	'M+1': '1110111',
	'M-1': '1110010',
	'D+M': '1000010',
	'D-M': '1010011',
	'M-D': '1000111',
	'D&M': '1000000',
	'D|M': '1010101'
}

FIRST_MEMORY_ADDRESS = 16
BUILT_INS = {
	'SP': 0,
	'LCL': 1,
	'ARG': 2,
	'THIS': 3,
	'THAT': 4,
	'R0': 0,
	'R1': 1,
	'R2': 2,
	'R3': 3,
	'R4': 4,
	'R5': 5,
	'R6': 6,
	'R7': 7,
	'R8': 8,
	'R9': 9,
	'R10': 10,
	'R11': 11,
	'R12': 12,
	'R13': 13,
	'R14': 14,
	'R15': 15,
	'SCREEN': 16384,
	'KBD': 24576
}


def main():
	with open(INPUT_FILENAME, 'r') as f:
		input_contents = f.readlines()

	instructions = _remove_comments(input_contents)
	(labels, instructions) = _create_label_table(instructions)
	variables = {}
	address_counter = FIRST_MEMORY_ADDRESS
	program_counter = 0

	for instruction in instructions:
		address_counter = _translate_instruction(
			instruction, labels, variables, address_counter, program_counter)
		program_counter += 1


def _remove_comments(input_contents):
	cleaned_lines = []
	for line in input_contents:
		cleaned_line = _remove_comment(line)
		if cleaned_line:
			cleaned_lines.append(cleaned_line)
	return cleaned_lines


def _remove_comment(line):
	return re.sub(COMMENT_REGEX, '', line).strip()


def _create_label_table(instructions_with_labels):
	instructions = []
	label_table = {}
	program_counter = 0
	for instruction in instructions_with_labels:
		match = LABEL_REGEX.search(instruction)
		if match:
			label = match.group(1)
			label_table[label] = program_counter
		else:
			instructions.append(instruction)
			program_counter += 1
	return (label_table, instructions)


def _translate_instruction(instruction, labels, variables, address_counter, program_counter):
	a_instruction_matches = INSTRUCTION_A_REGEX.search(instruction)

	if a_instruction_matches:
		a_instruction_value = a_instruction_matches.group(1)
		if a_instruction_value in labels:
			print(format(labels[a_instruction_value], '016b'))
		elif a_instruction_value in BUILT_INS:
			print(format(BUILT_INS[a_instruction_value], '016b'))
		elif a_instruction_value.isdigit():
			print(format(int(a_instruction_value), '016b'))
		elif a_instruction_value in variables:
			print(format(variables[a_instruction_value], '016b'))
		else:
			variables[a_instruction_value] = address_counter
			print(format(variables[a_instruction_value], '016b'))
			address_counter += 1
	else:
		comp_bits = _map_comp_bits(instruction)
		dst_bits = _map_dst_bits(instruction)
		jump_bits = _map_jump_bits(instruction)
		print('111%s%s%s' % (comp_bits, dst_bits, jump_bits))

	return address_counter


def _map_comp_bits(instruction):
	instruction_without_dest = INSTRUCTION_C_DEST_REGEX.sub('', instruction)
	comp_value = INSTRUCTION_C_JUMP_REGEX.sub('', instruction_without_dest)
	return COMP_MAP[comp_value]


def _map_dst_bits(instruction):
	match = INSTRUCTION_C_DEST_REGEX.search(instruction)
	if match:
		dst_value = match.group(1)
		return DESTINATION_MAP[dst_value]
	return '000'


def _map_jump_bits(instruction):
	match = INSTRUCTION_C_JUMP_REGEX.search(instruction)
	if match:
		jump_value = match.group(1)
		return JUMP_MAP[jump_value]
	return '000'


if __name__ == "__main__":
	main()