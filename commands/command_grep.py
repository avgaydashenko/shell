import re
import argparse


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
