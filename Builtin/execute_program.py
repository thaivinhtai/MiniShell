"""This modules will run a program that the user type in."""

from subprocess import run
from .Stuffs import get_path_environ, get_file_type, get_full_path


def execute_program(name_of_program, arguments):
    """
    execute_program(input) -> execute program in $PATH.

    This Function will check all the path in $PATH, if the program exists,
    execute it, else print the error message.

    Required arguments:
        name_of_program     -- name of program need to be called.
        arguments           -- arguments of the program.
    """
    environ_path = get_path_environ()
    path_program = ""
    try:
        # if there is a specified file, run it
        if get_file_type(name_of_program) == "file" and arguments != "" and\
            "/" in name_of_program:
            return run([get_full_path(name_of_program)] + arguments), 0
        if get_file_type(name_of_program) == "file" and "/" in name_of_program:
            return run([get_full_path(name_of_program)]), 0
        # if not a specified file, search all the path environment
        for element in environ_path:
            path_program = element + "/" + name_of_program
            if get_file_type(path_program) == "file" and arguments != "":
                return run([path_program] + arguments), 0
            if get_file_type(path_program) == "file":
                return run([path_program]), 0

        return print("intek-sh:", name_of_program + ": command not found"), 127
    except PermissionError:
        return print("intek-sh:", name_of_program + ": Permission denied"), 126
