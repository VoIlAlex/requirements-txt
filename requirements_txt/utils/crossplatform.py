import sys


def get_destination_command() -> str:
    if sys.platform in ['win32', 'cygwin']:
        command = 'where'
    else:
        command = 'which'
    return command
