from commands import *


# this dictionary is used in lexer to define commands in input
commands_dictionary = {
    "exit":   command_exit.command_exit,
    "|":      command_pipe.command_pipe,
    "echo":   command_echo.command_echo,
    "assign": command_assign.command_assign,
    "cat":    command_cat.command_cat,
    "wc":     command_wc.command_wc,
    "pwd":    command_pwd.command_pwd,
    "grep":   command_grep.command_grep
}