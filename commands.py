# getcwd will be used in pwd_command
from os import getcwd


# one and only purpose of this command is to change shell_status.is_run
# so any potential arguments are ignored
def command_exit(shell_status, _):
    shell_status.is_run = False


# makes from the current output an input for the next command
# potential current input is ignored
# command doesn't need any arguments
def command_pipe(shell_status):
    shell_status.input_stream = shell_status.output_stream
    shell_status.output_stream = ""


# current input and output are ignored
# the command writes all its arguments to the new output
def command_echo(shell_status, args):
    shell_status.input_stream = ""
    shell_status.output_stream = ""
    for arg in args:
        shell_status.output_stream = shell_status.output_stream + str(arg) + " "


# command changes environment by giving the first argument value of the second one
# all other arguments are ignored
def command_assign(shell_status, args):
    shell_status.environment[args[0]] = args[1]


# current input and output are ignored
# in arguments can be several files
# so command writes all their content to the new output
def command_cat(shell_status, args):
    shell_status.input_stream = ""
    shell_status.output_stream = ""

    for arg in args:
        with open(arg) as file:
            shell_status.output_stream += file.read()


# current output is ignored
# command writes to the new output necessary values from current input
# any potential arguments are ignored
def command_wc(shell_status, _):
    lines_num = len(shell_status.input_stream.split('\n'))
    words_num = len(shell_status.input_stream.split(' '))
    bytes_num = len(shell_status.input_stream) + 1
    shell_status.input_stream = ""
    shell_status.output_stream = "{} {} {}".format(lines_num, words_num, bytes_num)


# current input and output are ignored
# command writes to the new output current directory
# any potential arguments are ignored
def command_pwd(shell_status, _):
    shell_status.input_stream = ""
    shell_status.output_stream = getcwd()

# this dictionary is used in lexer to define commands in input
command_by_name = {
    "exit":   command_exit,
    "|":      command_pipe,
    "echo":   command_echo,
    "assign": command_assign,
    "cat":    command_cat,
    "wc":     command_wc,
    "pwd":    command_pwd
}