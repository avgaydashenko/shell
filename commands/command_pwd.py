from os import getcwd


# current input and output are ignored
# command writes to the new output current directory
# any potential arguments are ignored
def command_pwd(shell_status, _):
    shell_status.input_stream = ""
    shell_status.output_stream = getcwd()
