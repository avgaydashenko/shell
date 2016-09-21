

# one and only purpose of this command is to change shell_status.is_run
# so any potential arguments are ignored
def command_exit(shell_status, _):
    shell_status.is_run = False
