# will be used in command_grep
import os
import re
import argparse

# getcwd will be used in command_pwd
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


# current output is ignored
# current input may be ignored
def command_grep(shell_status, args):

    # creating parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-A', type=int, action='store', dest='lines_number')
    parser.add_argument('-w', '--word-regexp', action='store_true')
    parser.add_argument('-i', '--ignore-case', action='store_true')
    parser.add_argument('pattern', action='store')
    parser.add_argument('files', action='store', nargs='*')
    args = parser.parse_args(args)

    # if we need to search the whole word
    if args.word_regexp:
        args.pattern = "\\b{}\\b".format(args.pattern)

    # if grep got some file names in arguments input_stream is ignored
    if len(args.files) > 0:
        shell_status.input_stream = ""
        for arg in args.files:
            with open(arg) as file:
                shell_status.input_stream += file.read()

    lines = shell_status.input_stream.split('\n')
    shell_status.output_stream = ""

    for i in range(len(lines)):
        # if grep got -i in arguments perform case-insensitive matching (re.I)
        # 1 is magic just because module re works this way
        result = re.search(args.pattern, lines[i], re.I if args.ignore_case else 1)
        if result is not None:
            if args.lines_number is None:
                shell_status.output_stream += lines[i]
            else:
                for j in range(args.lines_number):
                    if i + j < len(lines):
                        shell_status.output_stream += lines[i + j]

    shell_status.input_stream = ""


# current input and output are ignored
# command change current directory
# any potential arguments are ignored
def command_cd(shell_status, args):
    shell_status.input_stream = ""
    shell_status.output_stream = ""

    os.chdir(str(args[0]))


# current input and output are ignored
# command writes to the new output list of file in current directory
# any potential arguments are ignored
def command_ls(shell_status, _):
    shell_status.input_stream = ""
    shell_status.output_stream = ' '.join(os.listdir(str(getcwd())))


# this dictionary is used in lexer to define commands in input
command_by_name = {
    "exit":   command_exit,
    "|":      command_pipe,
    "echo":   command_echo,
    "assign": command_assign,
    "cat":    command_cat,
    "wc":     command_wc,
    "pwd":    command_pwd,
    "grep":   command_grep,
    "cd":     command_cd,
    "ls":     command_ls
}