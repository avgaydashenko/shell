from lexer import get_tokens
from splitter import get_commands
from performer import execute_commands


# I use class with all information about shell's current status
# to pass it through the functions instead of many parameters
class ShellStatus:
    # this field describes is shell still run on not
    # value in it could be changed only by exit command
    is_run = True

    # local shell variables are stored in this dictionary
    environment = {}

    # by these strings particular commands can get input data and write output
    input_stream = ""
    output_stream = ""


# main cycle where we get commands one by one and perform them
while ShellStatus.is_run:
    command = input("Type your command: ")
    token_queue = get_tokens(command, ShellStatus.environment)
    command_queue = get_commands(token_queue)
    execute_commands(command_queue, ShellStatus)

    # by default the last one command is an empty pipe
    # and it changes output_stream to input_stream so we print input_stream
    if ShellStatus.input_stream != '':
        print(ShellStatus.input_stream)
