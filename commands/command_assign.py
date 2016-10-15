

# command changes environment by giving the first argument value of the second one
# all other arguments are ignored
def command_assign(shell_status, args):
    shell_status.environment[args[0]] = args[1]
