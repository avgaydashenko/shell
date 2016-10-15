

# current input and output are ignored
# the command writes all its arguments to the new output
def command_echo(shell_status, args):
    shell_status.input_stream = ""
    shell_status.output_stream = ""
    for arg in args:
        shell_status.output_stream = shell_status.output_stream + str(arg) + " "
