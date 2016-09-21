

# makes from the current output an input for the next command
# potential current input is ignored
# command doesn't need any arguments
def command_pipe(shell_status):
    shell_status.input_stream = shell_status.output_stream
    shell_status.output_stream = ""