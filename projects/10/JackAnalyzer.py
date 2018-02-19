import sys

from JackTokenizer import tokenize


def main(input_path):
	with open(input_path) as input_file:
		print(tokenize(input_file.readlines()))


if __name__ == '__main__':
	main(sys.argv[1])