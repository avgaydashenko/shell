from subprocess import call
from commands import command_pipe


def execute_commands(command_queue, shell_status):
    # first item of current_command is a real command and other items are arguments
    for current_command in command_queue:
        # trying to perform command but if we don't know it exception would be raised
        try:
            current_command[0](shell_status, current_command[1:])
        except TypeError:
            call(current_command)
        command_pipe(shell_status)