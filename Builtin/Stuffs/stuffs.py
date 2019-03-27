"""This module provides some aliases that will be used many times in the "Mini
-shell" program.

Functions in this module:
 - get_full_path(file) -> return full path of file.
 - get_file_type(file) -> return type of file.
 - get_path_environ()  -> get the value of $PATH in Operating System as list.
"""

from os import path, environ


def get_full_path(file):
    """
    get_full_path(file) -> return full path of file.

    This function figures out exactly the path of file on system.

    Required argument:
        file    --  a string-type file name.
    """
    if file[0] == '~':
        file = path.expanduser(file)
    else:
        file = path.realpath(file)
    return file


def get_file_type(file):
    """
    get_file_type(file) -> return type of file.

    This function check if a file is a directory, file and return its type via
    a string. If the file is not exist, return None.

    Required argument:
        file    -- a string-type file name.
    """
    try:
        file = get_full_path(file)
        if path.isfile(file):
            return "file"
        if path.isdir(file):
            return "directory"
        return 0
    except FileNotFoundError:
        return None


def get_path_environ():
    """
    get_path_environ()  -> get the value of $PATH in Operating System as list.

    This Function splits all the value in the $PATH and return a list of path.
    """
    return environ['PATH'].split(":")
