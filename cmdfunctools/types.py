# -*- coding: utf-8 -*-
"""
cmdfunctools.types
~~~~~~~~~~~~~~~~~~~~~~~

Module with the type checkers for the function/commandline args.
"""

import string


# The different types checkers are defined here
def is_hex(arg: str) -> bool:
    """
    check if a string value represent an hexadecimal value.

    :return: True/False
    """
    res = all(c in (string.hexdigits + '\n') for c in arg)
    return res


# dictionary with all checkers
dct_types = {
    'hex': is_hex,
}
