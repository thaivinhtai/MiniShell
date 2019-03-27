"""This module provides the ability to change the working directory."""

from os import chdir
from .Stuffs import get_file_type, get_full_path


def change_dir(directory):
    """
    change_dir(directory)   ->  change current dir to an other dir.

    If the directory is existed, change to directory. If it not exists, print
    error message.
    """
    while "" in directory:
        directory.remove("")
    if not directory:
        directory.append("~")
    if get_file_type(directory[0]) == "directory":
        return chdir(get_full_path(directory[0]))
    if get_file_type(directory[0]) is None:
        return print("intek-sh: cd:", directory[0] + ": No such file or",
                     "directory")
    return print("intek-sh: cd:", directory[0] + ": Not a directory"), 0
