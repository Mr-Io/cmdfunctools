# -*- coding: utf-8 -*-
"""
cmdfunctools.types
~~~~~~~~~~~~~~~~~~~~~~~

Module with the type checkers for the function/commandline args.
"""

import string


# ***********************************************************
# default functions used when type argument are not provided
def default_true(*arg):
    """
    Auxiliar function to be used if type is not provided.

    :return: True
    """
    return True


def default_arg(*arg):
    """
    Auxiliar function to be used if type is not provided.

    :return: input arg
    """
    return arg[0]


# ***********************************************************
# The different types checkers are defined here:
def is_hex(arg: str) -> bool:
    """
    Check if a string value represent an hexadecimal value.

    :return: True/False
    """
    res = all(c in (string.hexdigits + '\n') for c in arg)
    return res


def is_int(arg: str) -> bool:
    """
    Check if a string value represent an hexadecimal value.

    :return: True/False
    """
    res = all(c in (string.digits + '\n') for c in arg)
    return res


# dictionary with all functions for the type-check
dct_type_check = {
    'int': is_int,
    'hex': is_hex,
}


# ***********************************************************
# The converters from type to bytes are defined here
def from_hex(arg: str, length: int) -> bytes:
    """
    Transform a hexadecimal string into a bytearray of a given length.

    :return: a bytearray
    """
    narg = int(arg, 16)
    if length == 0:
        length = 512
    barg = narg.to_bytes(int(length/2), 'big')
    return barg


def from_int(arg: str, length: int = -1) -> bytes:
    """
    Transform a integer string into a bytearray of a given length.

    :return: a bytearray
    """
    narg = int(arg)
    barg = narg.to_bytes(length, 'big')
    return barg


# dictionary with all functions for transforming specific-string-types into bytes
dct_convert_from = {
    'int': from_int,
    'hex': from_hex,
}


# ***********************************************************
# The converters from bytes to another type are defined here
def to_int(arg: bytes) -> int:
    narg = int.from_bytes(arg, 'big')
    return narg


# dictionary with all functions for transforming bytes into other type
dct_convert_to = {
    'int': to_int,
}
