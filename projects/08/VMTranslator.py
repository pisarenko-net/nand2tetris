import os
import re
import sys

from VMArithmeticCommands import _add
from VMArithmeticCommands import _sub
from VMArithmeticCommands import _neg
from VMArithmeticCommands import _eq
from VMArithmeticCommands import _gt
from VMArithmeticCommands import _lt
from VMArithmeticCommands import _and
from VMArithmeticCommands import _or
from VMArithmeticCommands import _not
from VMBranch import goto as _goto
from VMBranch import if_goto as _if_goto
from VMBranch import label as _label
from VMFunction import bootstrap
from VMFunction import call as _call
from VMFunction import function as _function
from VMFunction import ret as _return
from VMPush import pop as _pop
from VMPush import push as _push


COMMENT_REGEX = re.compile(r'(//.*)')

VM_COMMANDS = {
	'push': _push,
	'pop': _pop,

	'add': _add,
	'sub': _sub,
	'neg': _neg,

	'eq': _eq,
	'gt': _gt,
	'lt': _lt,

	'and': _and,
	'or': _or,
	'not': _not,

	'label': _label,
	'if-goto': _if_goto,
	'goto': _goto,

	'call': _call,
	'function': _function,
	'return': _return
}


def main(input_path):
	with open(_create_output_path(input_path), 'w') as output_file:
		if os.path.isdir(input_path):
			output_file.write(bootstrap())

		command_counter = 1

		for input_file_path in _get_source_files(input_path):
			with open(input_file_path) as input_file:
				vm_source_code = input_file.readlines()
			class_name = _parse_class_name(input_file_path)
			command_counter = _translate_class(output_file, class_name, command_counter, vm_source_code)


def _create_output_path(input_path):
	if os.path.isfile(input_path):
		return input_path.replace('.vm', '.asm')
	else:
		folder = os.path.basename(os.path.normpath(input_path))
		filename = folder + '.asm'
		return os.path.join(input_path, filename)


def _get_source_files(input_path):
	if os.path.isfile(input_path):
		return [input_path]
	else:
		return [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith('.vm')]


def _parse_class_name(input_path):
	filename_w_ext = os.path.basename(input_path)
	filename, _ = os.path.splitext(filename_w_ext)
	return filename


def _translate_class(output_file, class_name, command_counter, vm_source_code):
	for line in vm_source_code:
		clean_line = _remove_comment(line)
		if not clean_line:
			continue
		line_tokens = clean_line.split(' ')
		vm_command = line_tokens[0]
		vm_command_arguments = line_tokens[1:]
		output_file.write(VM_COMMANDS[vm_command](class_name, command_counter, *vm_command_arguments))
		command_counter += 1
	return command_counter


def _remove_comment(line):
        return re.sub(COMMENT_REGEX, '', line).strip()


if __name__ == '__main__':
	main(sys.argv[1])
