_CLASS_VAR_KINDS = ['static', 'field']
_SUBROUTINE_VAR_KINDS = ['var', 'arg']


class SymbolTable(object):
	def __init__(self):
		self.class_scope = Scope(_CLASS_VAR_KINDS)
		self.subroutine_scopes = []
		self.current_subroutine_scope = Scope(_SUBROUTINE_VAR_KINDS)

	def enter_subroutine(self):
		self.subroutine_scopes.append(self.current_subroutine_scope)
		self.current_subroutine_scope = Scope(['var', 'arg'])

	def exit_subroutine(self):
		self.current_subroutine_scope = self.subroutine_scopes.pop()

	def count(self, kind):
		scope = self._get_scope_by_kind(kind)
		return scope.counts[kind]

	def _get_scope_by_kind(self, kind):
		if kind in self.class_scope.counts:
			return self.class_scope
		elif kind in self.current_subroutine_scope.counts:
			return self.current_subroutine_scope
		else:
			return None

	def define(self, kind, type, identifier):
		scope = self._get_scope_by_kind(kind)
		scope.identifiers[identifier] = {
			'kind': kind,
			'type': type,
			'index': scope.counts[kind]
		}
		scope.counts[kind] += 1

	def kind_of(self, identifier):
		scope = self._get_scope_by_identifier(identifier)
		if scope:
			return scope.identifiers[identifier]['kind']
		else:
			return None

	def _get_scope_by_identifier(self, identifier):
		if identifier in self.current_subroutine_scope.identifiers:
			return self.current_subroutine_scope
		elif identifier in self.class_scope.identifiers:
			return self.class_scope

	def type_of(self, identifier):
		scope = self._get_scope_by_identifier(identifier)
		if scope:
			return scope.identifiers[identifier]['type']

	def index_of(self, identifier):
		scope = self._get_scope_by_identifier(identifier)
		if scope:
			return scope.identifiers[identifier]['index']


class Scope(object):
	def __init__(self, var_kinds):
		self.counts = {kind: 0 for kind in var_kinds}
		self.identifiers = {}