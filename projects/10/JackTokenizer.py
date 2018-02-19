import re


IGNORED_EXPRESSIONS = [
	# comments
	(None, re.compile(r'//[^\n]*')),
	(None, re.compile(r'/\*.*?\*/', flags=re.MULTILINE|re.DOTALL)),
	# whitespace
	(None, re.compile(r'[ \n\t]+'))
]

KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var',
	        'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let',
	        'do', 'if', 'else', 'while', 'return']
KEYWORD_EXPRESSIONS = [('KEYWORD', re.compile('(%s)' % keyword)) for keyword in KEYWORDS]

SYMBOLS_EXPRESSION = ('SYMBOL', re.compile(r'([\{\}\(\)\[\]\.,;\+\-\*/&\|<>=_])'))

INTEGER_CONSTANT_EXPRESSION = ''
STRING_CONSTANT_EXPRESSION = ''

IDENTIFIER_EXPRESSION = ('IDENTIFIER', re.compile(r'(\w+)'))

TOKEN_EXPRESSIONS = IGNORED_EXPRESSIONS + KEYWORD_EXPRESSIONS + [SYMBOLS_EXPRESSION, IDENTIFIER_EXPRESSION]
# TOKEN_EXPRESSIONS.append(SYMBOLS_EXPRESSION)
# TOKEN_EXPRESSIONS.append(IDENTIFIER_EXPRESSION)
# TOKEN_EXPRESSIONS.append(IDENTIFIER_EXPRESSION)


def tokenize(input_lines):
	content = ''.join(input_lines)
	tokens = []
	current_position = 0

	while current_position < len(content):
		match = None

		for token_name, token_expression in TOKEN_EXPRESSIONS:
			match = token_expression.match(content, current_position)
			if match:
				if token_name:
					tokens.append((token_name, match.group(1)))
				current_position = match.end(0)
				break

	return tokens