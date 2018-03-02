import re


IGNORED_EXPRESSIONS = [
	# comments
	(None, re.compile(r'(//[^\n]*)')),
	(None, re.compile(r'(/\*.*?\*/)', flags=re.MULTILINE|re.DOTALL)),
	# whitespace
	(None, re.compile(r'([\s\n\t]+)'))
]

KEYWORDS = ['class', 'constructor', 'function', 'method', 'field', 'static', 'var',
	        'int', 'char', 'boolean', 'void', 'true', 'false', 'null', 'this', 'let',
	        'do', 'if', 'else', 'while', 'return']
KEYWORD_EXPRESSIONS = [('keyword', re.compile('(%s)\s' % keyword)) for keyword in KEYWORDS]

SYMBOLS_EXPRESSION = ('symbol', re.compile(r'([\{\}\(\)\[\]\.,;\+\-\*/&\|<>=_~])'))
INT_CONST_EXPRESSION = ('integerConstant', re.compile(r'(\d+)'))
STRING_CONST_EXPRESSION = ('stringConstant', re.compile(r'"(.*?)"'))
IDENTIFIER_EXPRESSION = ('identifier', re.compile(r'([a-zA-Z_]\w*)'))

TOKEN_EXPRESSIONS = IGNORED_EXPRESSIONS + KEYWORD_EXPRESSIONS + \
                    [SYMBOLS_EXPRESSION, INT_CONST_EXPRESSION,
                     STRING_CONST_EXPRESSION, IDENTIFIER_EXPRESSION] 


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
