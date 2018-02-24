import os
import sys

from JackTokenizer import tokenize
from JackCompilationEngine import CompilationEngine


def main(input_path):
	for input_file_path in _get_source_files(input_path):
		print('PROCESSING %s' % input_file_path)
		with open(input_file_path) as input_file:
			tokens = tokenize(input_file.readlines())
			compilation_engine = CompilationEngine(tokens)
			compiled_class = compilation_engine.compile_class()
			with open(_create_output_path(input_file_path), 'w') as output_file:
				output_file.write(compiled_class)


def _get_source_files(input_path):
	if os.path.isfile(input_path):
		return [input_path]
	else:
		return [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith('.jack')]


def _create_output_path(input_path):
	return input_path.replace('.jack', '.xml')


if __name__ == '__main__':
	main(sys.argv[1])
