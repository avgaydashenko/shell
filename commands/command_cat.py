

# current input and output are ignored
# in arguments can be several files
# so command writes all their content to the new output
def command_cat(shell_status, args):
    shell_status.input_stream = ""
    shell_status.output_stream = ""

    for arg in args:
        with open(arg) as file:
            shell_status.output_stream += file.read()
