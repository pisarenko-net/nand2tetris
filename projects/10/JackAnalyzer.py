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
			print(tokens)
			print(compiled_class)


def _get_source_files(input_path):
	if os.path.isfile(input_path):
		return [input_path]
	else:
		return [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith('.jack')]


if __name__ == '__main__':
	main(sys.argv[1])
