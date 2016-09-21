

# current output is ignored
# command writes to the new output necessary values from current input
# any potential arguments are ignored
def command_wc(shell_status, _):
    lines_num = len(shell_status.input_stream.split('\n'))
    words_num = len(shell_status.input_stream.split(' '))
    bytes_num = len(shell_status.input_stream) + 1
    shell_status.input_stream = ""
    shell_status.output_stream = "{} {} {}".format(lines_num, words_num, bytes_num)
