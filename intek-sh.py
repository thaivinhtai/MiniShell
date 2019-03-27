#!/usr/bin/env python3

"""This program is called The Mini-shell, that simulates the Bash Shell."""

from Builtin import execute_program, change_dir, exit_intek_shell


def run_command(command, arguments):
    """
    switch_command(command) ->  choose a command.

    This is a manual swithcer for select function quickly.

    Required arguments:
        command     --  a string-type, which is name of command.
        arguments    --  argument of command.
    """
    switcher = {
        'cd': change_dir,
        'exit': exit_intek_shell
    }
    try:
        func = switcher.get(command)
        return func(arguments)
    except TypeError:
        return execute_program(command, arguments)


def main():
    while True:
        orchestra = input("intek-sh$ ")
        command = ""
        arguments = ""
        try:
            separation = orchestra.index(" ")
            command = orchestra[:separation]
            arguments = orchestra.replace(orchestra[:(separation + 1)], "")
        except ValueError:
            command = orchestra
        result = run_command(command, arguments)
        if result == "exit":
            break
    return 0


if __name__ == "__main__":
    main()
