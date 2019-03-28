"""This module print the environment."""

from os import environ


def print_env(variables):
    """
    print_env(variables)  ->  print the value of env.

    This function print the values of the specified environment VARIABLE(s). If
    no VARIABLE is specified, print name and value pairs for them all.

    Required argument:
        variables   --  list of environment variables.
    """
    variables = list(variables)
    if not variables:
        for var, value in environ.items():
            print(var + "=" + value)
        return 0, 0

    result = []
    for element in variables:
        try:
            result.append(str(environ[element]))
        except KeyError:
            continue
    if result:
        return print(*result, sep='\n'), 0
    return 0, 0
