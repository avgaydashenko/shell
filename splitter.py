import unittest
from command_by_name import commands_dictionary


def get_commands(token_queue):
    command_queue = []
    current_command = []

    # split all commands by pipe
    for token in token_queue:
        if token == commands_dictionary["|"]:
            command_queue.append(current_command)
            current_command = []
        else:
            current_command.append(token)
    command_queue.append(current_command)

    return command_queue


class TestParser(unittest.TestCase):

    def test_parser(self):
        self.token_queue = [commands_dictionary['exit'], "now", commands_dictionary['|'], "please"]
        self.assertEqual(get_commands(self.token_queue), [[commands_dictionary['exit'], "now"], ["please"]])
