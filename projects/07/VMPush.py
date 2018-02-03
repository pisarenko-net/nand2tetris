def push(command_number, memory_segment, value):
	return '''// push {segment} {value}
@{value}
D=A
@SP
A=M
M=D
@SP
M=M+1
'''.format(segment=memory_segment, value=value)