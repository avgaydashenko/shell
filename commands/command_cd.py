from os import chdir


# current input and output are ignored
# command changes current directory to given in first argument
# all other arguments are ignored
def command_cd(shell_status, args):
    chdir(str(args[0]))
    shell_status.input_stream = ""
    shell_status.output_stream = ""
