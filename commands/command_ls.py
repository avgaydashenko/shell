from os import listdir, getcwd


# current input and output are ignored
# command writes to the new output list of files in current directory
# any potential arguments are ignored
def command_ls(shell_status, _):
    shell_status.input_stream = ""
    shell_status.output_stream = "\n".join(listdir(getcwd()))
