_STATEMENT_COMPILE_FUNCTIONS = {
	'while': '_compile_while_statement',
	'if': '_compile_if_statement',
	'return': '_compile_return_statement',
	'let': '_compile_let_statement',
	'do': '_compile_do_statement'
}

class CompilationEngine(object):
	def __init__(self, tokens):
		self.tokens = list(tokens)
		self.position = 0

	def compile_class(self):
		self._consume_token('class')
		self._consume_token()  # class identifier
		self._consume_token('{')

		while (self._get_current_token() in ['field', 'static']):
			self._compile_class_var_declaration()

		while (self._get_current_token() in ['constructor', 'function', 'method']):
			self._compile_subroutine_declaration()

		self._consume_token('}')
		return 'bugaboo'

	def _consume_token(self, expected=None):
		print(self.tokens[self.position])
		self.position += 1

	def _get_current_token(self):
		return self.tokens[self.position][1]

	def _compile_class_var_declaration(self):
		self._consume_token()  # field, static
		self._consume_token()  # type
		self._consume_token()  # variable name

		while (self._get_current_token() == ','):
			self._consume_token(',')
			self._consume_token()  # variable name

		self._consume_token(';')

	def _compile_subroutine_declaration(self):
		self._consume_token()  # constructor, function, method
		self._consume_token()  # type, void
		self._consume_token()  # subroutine name

		self._consume_token('(')
		if (self._get_current_token() != ')'):
			self._compile_parameter_list()
		self._consume_token(')')

		self._consume_token('{')

		while (self._get_current_token() == 'var'):
			self._compile_var_declaration()

		self._compile_statements()

		self._consume_token('}')

	def _compile_parameter_list(self):
		self._consume_token()  # type
		self._consume_token()  # parameter name

		while (self._get_current_token() == ','):
			self._consume_token(',')
			self._consume_token()  # type
			self._consume_token()  # parameter name

	def _compile_var_declaration(self):
		self._consume_token('var')
		self._consume_token()  # type
		self._consume_token()  # name

		while (self._get_current_token() == ','):
			self._consume_token(',')
			self._consume_token()  # name

		self._consume_token(';')

	def _compile_statements(self):
		while (self._get_current_token() in _STATEMENT_COMPILE_FUNCTIONS.keys()):
			function_name = _STATEMENT_COMPILE_FUNCTIONS[self._get_current_token()]
			_invoke_method(self, function_name)

	def _compile_while_statement(self):
		self._consume_token('while')
		self._consume_token('(')
		self._compile_expression()
		self._consume_token(')')

		self._consume_token('{')
		self._compile_statements()
		self._consume_token('}')

	def _compile_if_statement(self):
		self._consume_token('if')
		self._consume_token('(')
		self._compile_expression()
		self._consume_token(')')

		self._consume_token('{')
		self._compile_statements()
		self._consume_token('}')

		if (self._get_current_token() == 'else'):
			self._consume_token('else')
			self._consume_token('{')
			self._compile_statements()
			self._consume_token('}')

	def _compile_return_statement(self):
		self._consume_token('return')
		if (self._get_current_token() != ';'):
			self._compile_expression()
		self._consume_token(';')

	def _compile_let_statement(self):
		self._consume_token('let')
		self._consume_token()  # variable name

		if (self._get_current_token() == '['):
			self._consume_token('[')
			self._compile_expression()
			self._consume_token(']')

		self._consume_token('=')
		self._compile_expression()
		self._consume_token(';')

	def _compile_expression(self):
		pass

def _invoke_method(self, name):
	func = getattr(self, name)
	return func()