import unittest
import commands


# function searches variables in shell's environment and puts them in the input there it's necessary
def substitute_variables(input_stream, environment):
    quote_is_not_open = True

    i = 0
    while i < len(input_stream):
        if input_stream[i] == "'":
            quote_is_not_open = not quote_is_not_open
        elif input_stream[i] == '$' and quote_is_not_open:
            var = ""
            i += 1
            while i < len(input_stream) and input_stream[i].isalpha():
                var += input_stream[i]
                i += 1
            if var in environment:
                input_stream = input_stream[:i - len(var) - 1] + str(environment[var]) + input_stream[i:]
            continue
        i += 1

    return input_stream


# function replaces expressions of the form "a=b" by "assign a b"
# it's required to bring this command to the standard form
def process_assignment(input_stream):
    tokens = input_stream.split(' ')

    for i in range(len(tokens)):
        if '=' in tokens[i]:
            left = tokens[i][:tokens[i].find('=')]
            right = tokens[i][tokens[i].find('=')+1:]
            tokens[i] = "assign {} {}".format(left, right)

    input_stream = ' '.join(tokens)
    return input_stream


# split input into commands and arguments
def get_tokens(input_stream, environment):
    input_stream = substitute_variables(input_stream, environment)
    input_stream = process_assignment(input_stream)
    tokens = []

    i = 0
    while i < len(input_stream):
        if input_stream[i] == '"':
            token = input_stream[i + 1: input_stream.find('"', i + 1)]
            i = input_stream.find('"', i + 1) + 2
        elif input_stream[i] == "'":
            token = input_stream[i + 1: input_stream.find("'", i + 1)]
            i = input_stream.find("'", i + 1) + 2
        else:
            if input_stream.find(" ", i + 1) == -1:
                token = input_stream[i:]
                i = len(input_stream)
            else:
                token = input_stream[i: input_stream.find(" ", i + 1)]
                i = input_stream.find(" ", i + 1) + 1
            if token in commands.command_by_name:
                token = commands.command_by_name[token]
        tokens.append(token)

    return tokens


class TestLexer(unittest.TestCase):
    def test_substitute_variables(self):
        self.environment = {"a": 5, "b": 3}
        self.input_stream = '$a "$b" \'$a\''
        self.assertEqual(substitute_variables(self.input_stream, self.environment), '5 "3" \'$a\'')

    def test_process_assignment(self):
        self.input_stream = "a=5 please"
        self.assertEqual(process_assignment(self.input_stream), "assign a 5 please")

    def test_lexer_simple_input(self):
        self.environment = {}
        self.input_stream = "exit 'now'"
        self.assertEqual(get_tokens(self.input_stream, self.environment), [commands.command_by_name['exit'], "now"])

    def test_lexer_pipe(self):
        self.environment = {}
        self.input_stream = "exit | 'now'"
        self.assertEqual(get_tokens(self.input_stream, self.environment),
                         [commands.command_by_name['exit'], commands.command_by_name['|'], "now"])
