from xml.sax.saxutils import escape

from JackVariables import SymbolTable


_STATEMENT_COMPILE_FUNCTIONS = {
	'while': '_compile_while_statement',
	'if': '_compile_if_statement',
	'return': '_compile_return_statement',
	'let': '_compile_let_statement',
	'do': '_compile_do_statement'
}

_OPERATORS = ['+', '-', '*', '/', '&', '|', '<', '>', '=']
_UNARY_OPERATORS = ['-', '~']

class CompilationEngine(object):
	def __init__(self, tokens):
		self.tokens = list(tokens)
		self.position = 0
		self.output = ''
		self.var_symbol_table = SymbolTable()
		self.name = None
		self.subroutines = set()
		self.current_scope = None

	def compile_class(self):
		self._opening('class')
		self._consume_token('class', indent=1)
		self._set_class_name()
		self._consume_token('{', indent=1)

		while (self._get_current_token() in ['field', 'static']):
			self._compile_class_var_declaration()

		while (self._get_current_token() in ['constructor', 'function', 'method']):
			self._compile_subroutine_declaration()

		self._consume_token('}', indent=1)
		self._closing('class')
		return self.output

	def _opening(self, tag, indent=0):
		#self.output += '  ' * indent + '<%s>\n' % tag
		self.current_scope = tag

	def _closing(self, tag, indent=0):
		pass#self.output += '  ' * indent + '</%s>\n' % tag

	def _consume_token(self, expected=None, indent=0):
		token_type, token_value = self.tokens[self.position]
		self.position += 1
		#self.output += '  ' * indent + '<{0}> {1} </{0}>\n'.format(token_type, escape(token_value))
		if token_type == 'identifier':
			if token_value == self.name:
				pass#self.output += 'CLASS DETECTED\n'
			elif token_value in self.subroutines:
				pass#self.output += 'SUBROUTINE DETECTED\n'
			elif self.current_scope == 'doStatement':
				if self._get_current_token() == '.':
					pass#self.output += 'CLASS DETECTED\n'
				else:
					pass#self.output += 'SUBROUTINE DETECTED\n'
			else:
				defined = self.current_scope in ['classVarDec', 'varDec', 'parameterList']
				kind = self.var_symbol_table.kind_of(token_value)
				type = self.var_symbol_table.type_of(token_value)
				index = self.var_symbol_table.index_of(token_value)
				pass#self.output += '{0} {1} {2} {3}\n'.format(defined, kind, type, index)
		return (token_type, token_value)

	def _set_class_name(self):
		self.name = self._get_current_token()
		self._consume_token(indent=1)

	def _get_current_token(self, offset=0):
		return self.tokens[self.position + offset][1]

	def _compile_class_var_declaration(self):
		self._opening('classVarDec', 1)

		kind = self._get_current_token()
		type = self._get_current_token(1)
		identifier = self._get_current_token(2)
		self.var_symbol_table.define(kind, type, identifier)

		self._consume_token(indent=2)  # field, static
		self._consume_token(indent=2)  # type
		self._consume_token(indent=2)  # variable name

		while (self._get_current_token() == ','):
			self._consume_token(',', indent=2)
			identifier = self._get_current_token()
			self.var_symbol_table.define(kind, type, identifier)
			self._consume_token(indent=2)  # variable name

		self._consume_token(';', indent=2)
		self._closing('classVarDec', 1)

	def _compile_subroutine_declaration(self):
		self._opening('subroutineDec', 1)
		self.var_symbol_table.enter_subroutine()
		self.output += '%s ' % self._consume_token(indent=2)[1]  # constructor, function, method
		self._consume_token(indent=2)[1]  # type, void
		self.output += '{0}.{1} '.format(self.name, self._save_subroutine_name())

		self._consume_token('(', indent=2)
		self._opening('parameterList', 2)
		if (self._get_current_token() != ')'):
			self._compile_parameter_list()
		else:
			self.output += '0\n'
		self._closing('parameterList', 2)
		self._consume_token(')', indent=2)

		self._opening('subroutineBody', 2)
		self._consume_token('{', indent=3)

		while (self._get_current_token() == 'var'):
			self._compile_var_declaration()

		self._compile_statements(3)

		self._consume_token('}', indent=3)
		self._closing('subroutineBody', 2)
		self.var_symbol_table.exit_subroutine()
		self._closing('subroutineDec', 1)

	def _save_subroutine_name(self):
		subroutine_name = self._get_current_token()
		self.subroutines.add(subroutine_name)
		self._consume_token(indent=2)  # subroutine name
		return subroutine_name

	def _compile_parameter_list(self):
		type = self._get_current_token()
		identifier = self._get_current_token(1)
		self.var_symbol_table.define('arg', type, identifier)

		self._consume_token(indent=3)  # type
		self._consume_token(indent=3)  # parameter name
		count = 1

		while (self._get_current_token() == ','):
			count += 1
			self._consume_token(',', indent=3)
			type = self._get_current_token()
			identifier = self._get_current_token(1)
			self.var_symbol_table.define('arg', type, identifier)

			self._consume_token(indent=3)  # type
			self._consume_token(indent=3)  # parameter name

		self.output += '%s\n' % count

	def _compile_var_declaration(self):
		self._opening('varDec', 3)
		kind = self._get_current_token()
		type = self._get_current_token(1)
		identifier = self._get_current_token(2)
		self.var_symbol_table.define(kind, type, identifier)

		self._consume_token('var', indent=4)
		self._consume_token(indent=4)  # type
		self._consume_token(indent=4)  # name

		while (self._get_current_token() == ','):
			self._consume_token(',', indent=4)
			identifier = self._get_current_token()
			self.var_symbol_table.define(kind, type, identifier)
			self._consume_token(indent=4)  # name

		self._consume_token(';', indent=4)
		self._closing('varDec', 3)

	def _compile_statements(self, indent=0):
		self._opening('statements', indent)
		while (self._get_current_token() in _STATEMENT_COMPILE_FUNCTIONS.keys()):
			function_name = _STATEMENT_COMPILE_FUNCTIONS[self._get_current_token()]
			_invoke_method(self, function_name, indent+1)
		self._closing('statements', indent)

	def _compile_while_statement(self, indent=0):
		self._opening('whileStatement', indent)
		self._consume_token('while', indent=indent+1)
		self._consume_token('(', indent=indent+1)
		self._compile_expression(indent+1)
		self._consume_token(')', indent=indent+1)

		self._consume_token('{', indent=indent+1)
		self._compile_statements(indent+1)
		self._consume_token('}', indent=indent+1)
		self._closing('whileStatement', indent)

	def _compile_if_statement(self, indent=0):
		self._opening('ifStatement', indent)
		self._consume_token('if', indent=indent+1)
		self._consume_token('(', indent=indent+1)
		self._compile_expression(indent+1)
		self._consume_token(')', indent=indent+1)

		self._consume_token('{', indent=indent+1)
		self._compile_statements(indent+1)
		self._consume_token('}', indent=indent+1)

		if (self._get_current_token() == 'else'):
			self._consume_token('else', indent=indent+1)
			self._consume_token('{', indent=indent+1)
			self._compile_statements(indent+1)
			self._consume_token('}', indent=indent+1)
		self._closing('ifStatement', indent)

	def _compile_return_statement(self, indent=0):
		self._opening('returnStatement', indent)
		self._consume_token('return', indent=indent+1)
		if (self._get_current_token() != ';'):
			self._compile_expression(indent+1)
		self._consume_token(';', indent=indent+1)
		self._closing('returnStatement', indent)

	def _compile_let_statement(self, indent=0):
		self._opening('letStatement', indent)
		self._consume_token('let', indent=indent+1)
		self._consume_token(indent=indent+1)  # variable name

		if (self._get_current_token() == '['):
			self._consume_token('[', indent=indent+1)
			self._compile_expression(indent+1)
			self._consume_token(']', indent=indent+1)

		self._consume_token('=', indent=indent+1)
		self._compile_expression(indent+1)
		self._consume_token(';', indent=indent+1)
		self._closing('letStatement', indent)

	def _compile_do_statement(self, indent=0):
		self._opening('doStatement', indent)
		self._consume_token('do', indent=indent+1)
		self._compile_subroutine_call(indent+1)
		self._consume_token(';', indent=indent+1)
		self._closing('doStatement', indent)

	def _compile_subroutine_call(self, indent=0):
		if (self._get_current_token(1) == '('):
			self._consume_token(indent=indent)  # subroutine name
		else:
			self._consume_token(indent=indent)  # class name or var name
			self._consume_token('.', indent=indent)
			self._consume_token(indent=indent)  # subroutine name

		self._consume_token('(', indent=indent)
		self._compile_expression_list(indent)
		self._consume_token(')', indent=indent)

	def _compile_expression(self, indent=0):
		self._opening('expression', indent)
		self._compile_term(indent+1)
		while (self._get_current_token() in _OPERATORS):
			self._consume_token(indent=indent+1)  # operator
			self._compile_term(indent+1)
		self._closing('expression', indent)

	def _compile_expression_list(self, indent=0):
		self._opening('expressionList', indent)
		if (self._get_current_token() != ')'):
			self._compile_expression(indent+1)
			while (self._get_current_token() == ','):
				self._consume_token(',', indent=indent+1)
				self._compile_expression(indent+1)
		self._closing('expressionList', indent)

	def _compile_term(self, indent=0):
		self.output += 'term\n'
		self._opening('term', indent)
		if (self._get_current_token() == '('):
			self._consume_token('(', indent=indent+1)
			self._compile_expression(indent+1)
			self._consume_token(')', indent=indent+1)
		elif (self._get_current_token(1) == '['):
			self._consume_token(indent=indent+1)  # variable name
			self._consume_token('[', indent=indent+1)
			self._compile_expression(indent+1)
			self._consume_token(']', indent=indent+1)
		elif (self._get_current_token() in _UNARY_OPERATORS):
			self._consume_token(indent=indent+1)  # unary operator
			self._compile_term(indent+1)
		elif (self._get_current_token(1) == '(' or self._get_current_token(1) == '.'):
			self._compile_subroutine_call(indent+1)
		else:
			self._consume_token(indent=indent+1)  # constants or var name
		self._closing('term', indent)

def _invoke_method(self, name, argument):
	func = getattr(self, name)
	return func(argument)
