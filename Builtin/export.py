"""This module marks each NAME for automatic export to the environment of
subsequently executed commands. If VALUE is supplied, assign VALUE before
exporting.
"""

from os import environ


def export(arguments):
    """
    export(arguments)   ->  change value of environ variables.

    Required argument:
        arguments   --  list of argument.
    """
    if not arguments:
        for var, value in environ.items():
            print("declare -x", var + '="' + value + '""')
        return 0, 0
    for element in arguments:
        if "=" in element:
            environ[element[:element.index("=")]] = element[(element.index("=")
                                                             + 1):]
        else:
            environ[element] = ""
    return 0, 0
