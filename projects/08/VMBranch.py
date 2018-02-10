from VMCommon import ADDRESS
from VMCommon import COMMENT
from VMCommon import GOTO
from VMCommon import LABEL
from VMCommon import READ_AND_DECREMENT_SP


JUMP_IF_NOT = 'D;JNE\n'


def label(class_name, command_number, label_name):
	output = COMMENT.format(command='label', name=label_name, arg='')
	output += LABEL.format(address=label_name)
	return output


def goto(class_name, command_number, label_name):
	output = COMMENT.format(command='goto', name=label_name, arg='')
	output += GOTO.format(address=label_name)
	return output


def if_goto(class_name, command_number, label_name):
	output = COMMENT.format(command='if-goto', name=label_name, arg='')
	output += READ_AND_DECREMENT_SP
	output += ADDRESS.format(address=label_name)
	output += JUMP_IF_NOT
	return output
