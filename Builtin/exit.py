"""This module is an exit of the program."""


def exit_intek_shell(argument):
    """
    exit_intek_shell(argument) -> return "exit" and exit status.

    Optional argument:
        -   argument    --  exit status.
    """
    if argument == "":
        print("exit")
        return "exit"
    try:
        int(argument)
        print("exit")
        return "exit"
    except ValueError:
        print("exit")
        print("intek-sh: exit:", str(argument) + ": numeric argument required")
        return "exit"
