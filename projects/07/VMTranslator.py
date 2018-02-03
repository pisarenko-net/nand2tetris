import re
import sys

from VMPush import push as _push
from VMArithmeticCommands import _add
from VMArithmeticCommands import _sub
from VMArithmeticCommands import _neg
from VMArithmeticCommands import _eq
from VMArithmeticCommands import _gt
from VMArithmeticCommands import _lt
from VMArithmeticCommands import _and
from VMArithmeticCommands import _or
from VMArithmeticCommands import _not


COMMENT_REGEX = re.compile(r'(//.*)')

VM_COMMANDS = {
	'push': _push,
	'add':  _add,
	'sub':  _sub,
	'neg':  _neg,
	'eq':   _eq,
	'gt':   _gt,
	'lt':   _lt,
	'and':  _and,
	'or':   _or,
	'not':  _not
}


def main(input_path):
	with open(input_path) as f:
		vm_source_code = f.readlines()

	command_counter = 0

	with open(_create_output_path(input_path), 'w') as f:
		for line in vm_source_code:
			clean_line = _remove_comment(line)
			if not clean_line:
				continue
			line_tokens = clean_line.split(' ')
			vm_command = line_tokens[0]
			vm_command_arguments = line_tokens[1:]
			print(VM_COMMANDS[vm_command](command_counter, *vm_command_arguments))
			f.write(VM_COMMANDS[vm_command](command_counter, *vm_command_arguments))
			command_counter += 1


def _create_output_path(input_path):
	return input_path.replace('.vm', '.asm')


def _remove_comment(line):
        return re.sub(COMMENT_REGEX, '', line).strip()


if __name__ == '__main__':
	main(sys.argv[1])