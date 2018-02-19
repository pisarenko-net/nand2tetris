import re


IGNORED_EXPRESSIONS = [
	# comments
	(None, re.compile(r'//[^\n]*')),
	(None, re.compile(r'/\*.*?\*/', flags=re.MULTILINE|re.DOTALL)),
	# whitespace
	(None, re.compile(r'[ \n\t]+'))
]

KEYWORD_EXPRESSIONS = [
	('class', re.compile('class')),
	('constructor', re.compile('constructor')),
	('function', re.compile('function')),
	('method', re.compile('method')),
	('field', re.compile('field')),
	('static', re.compile('static')),
	('var', re.compile('var')),
	('int', re.compile('int')),
	('char', re.compile('char')),
	('boolean', re.compile('boolean')),
	('void', re.compile('void')),
	('true', re.compile('true')),
	('false', re.compile('false')),
	('null', re.compile('null')),
	('this', re.compile('this')),
	('let', re.compile('let')),
	('do', re.compile('do')),
	('if', re.compile('if')),
	('else', re.compile('else')),
	('while', re.compile('while')),
	('return', re.compile('return'))
]

KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var',
	        'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let',
	        'do', 'if', 'else', 'while', 'return']
SYMBOLS = '{}()[].,;+-*/&|<>=_'

SYMBOL_EXPRESSIONS = [
	('{', re.compile(r'\{')),
]

TOKEN_EXPRESSIONS = IGNORED_EXPRESSIONS + KEYWORD_EXPRESSIONS + SYMBOL_EXPRESSIONS + [
	('METHOD', re.compile(r'method')),
	('DO', re.compile(r'do')),
]


def tokenize(input_lines):
	content = ''.join(input_lines)
	tokens = []
	current_position = 0
	print(content)

	while current_position < len(content):
		match = None

		for token_name, token_expression in TOKEN_EXPRESSIONS:
			match = token_expression.match(content, current_position)
			if match:
				print(match.group(0))
				if token_name:
					tokens.append(token_name)
				current_position = match.end(0)
				break
			print(tokens, current_position)

	return tokens