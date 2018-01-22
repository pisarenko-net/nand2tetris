import re
import sys


INPUT_FILENAME = sys.argv[1]

COMMENT_REGEX = r'(//.*)'
LABEL_REGEX = r'^\s*\((.*)\)\s*$'
INSTRUCTION_A_REGEX = r'^@(.*)$'


def main():
	with open(INPUT_FILENAME, 'r') as f:
		input_contents = f.readlines()

	instructions = _remove_comments(input_contents)
	labels = _create_label_table(instructions)
	variables = {}

	for instruction in instructions:
		_translate_instruction(instruction, labels, variables)


def _remove_comments(input_contents):
	cleaned_lines = []
	for line in input_contents:
		cleaned_line = _remove_comment(line)
		if cleaned_line:
			cleaned_lines.append(cleaned_line)
	return cleaned_lines


def _remove_comment(line):
	return re.sub(COMMENT_REGEX, '', line).strip()


def _create_label_table(instructions):
	label_table = {}
	for idx, instruction in enumerate(instructions):
		match = re.search(LABEL_REGEX, instruction)
		if match:
			label = match.group(1)
			label_table[label] = idx + 1
	return label_table


def _translate_instruction(instruction, labels, variables):
	a_instruction_matches = re.search(INSTRUCTION_A_REGEX, instruction)

	if a_instruction_matches:
		a_instruction = a_instruction_matches.group(1)
		if a_instruction in labels:
			pass
		elif 

	print(instruction)


if __name__ == "__main__":
	main()