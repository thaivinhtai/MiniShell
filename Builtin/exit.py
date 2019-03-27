"""This module is an exit of the program."""


def exit_intek_shell(argument):
    """
    exit_intek_shell(argument) -> return "exit" and exit status.

    Optional argument:
        -   argument    --  exit status.
    """
    argument = list(argument)
    while "" in argument:
        argument.remove("")
    if not argument:
        print("exit")
        return "exit", 0
    try:
        int(argument[0])
        print("exit")
        return "exit", argument[0]
    except ValueError:
        print("exit")
        print("intek-sh: exit:", str(argument[0]) +
              ": numeric argument required")
        return "exit", 2
