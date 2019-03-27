#!/usr/bin/env python3

"""This program is called The Mini-shell, that simulates the Bash Shell."""

from Builtin import (execute_program, change_dir, exit_intek_shell,
                     print_env, export, unset)


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
        'exit': exit_intek_shell,
        'printenv': print_env,
        'export': export,
        'unset': unset
    }
    try:
        func = switcher.get(command)
        return func(arguments)
    except TypeError:
        return execute_program(command, arguments)


def main():
    """
    This is the core of the program, get in put and execute.
    """
    while True:
        try:
            orchestra = input("intek-sh$ ")
            if orchestra == "":
                continue
            command = ""
            arguments = ""
            try:
                separation = orchestra.index(" ")
                command = orchestra[:separation]
                arguments = orchestra.replace(orchestra[:(separation + 1)], "").\
                    split(" ")
            except ValueError:
                command = orchestra
            result, status = run_command(command, arguments)
            if result == "exit":
                return status
        except EOFError:
            break


if __name__ == "__main__":
    main()
