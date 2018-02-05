from VMCommon import READ_AND_DECREMENT_SP


COMMENT_TEMPLATE = '// {command} {label_name}\n'


def label(class_name, command_number, label_name):
	output = COMMENT_TEMPLATE.format(command='label', label_name=label_name)
	output += '({label_name})\n'.format(label_name=label_name)
	return output


def goto(class_name, command_number, label_name):
	output = COMMENT_TEMPLATE.format(command='goto', label_name=label_name)
	output += '''@{label_name}
0;JMP
'''.format(label_name=label_name)
	return output


def if_goto(class_name, command_number, label_name):
	output = COMMENT_TEMPLATE.format(command='if-goto', label_name=label_name)
	output += READ_AND_DECREMENT_SP
	output += '@{label_name}\n'.format(label_name=label_name)
	output += 'D;JNE\n'
	return output
