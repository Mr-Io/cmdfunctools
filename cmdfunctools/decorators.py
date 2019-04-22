# -*- coding: utf-8 -*-
"""
cmdfunctools.decorators
~~~~~~~~~~~~~~~~~~~~~~~

Module with the decorators definitions to make function usable from command line.
"""
import functools
import sys

from .types import dct_types
from .exceptions import CommandInputError


# decorator for transforming python functions in command line usable commands
def command_func(length: int = 0, strict: bool = True, itype: str = ''):
    """Decorator that transform pure functions into command line usable functions."""
    def wrapper(func):
        @functools.wraps(func)
        def func_wrapper():
            # Obtain arguments names of the original function:
            n_args = func.__code__.co_argcount
            # Obtain arguments from command input: sys.argv(normal call) or sys.stdin(pipelines)
            if sys.stdin.isatty():
                # Raise input exception if the number of arguments is incorrect
                if len(sys.argv) != (n_args+1):
                    raise CommandInputError('Received {} arguments (Expected {})'.format(
                        len(sys.argv)-1, n_args),
                        func,)
                input_args = sys.argv[1:]
            else:
                input_args = sys.stdin.readlines()
            strip_args = [arg.strip() for arg in input_args]
            for arg in strip_args:
                # Raise command input exceptions if incorrect type
                if itype != '' and not dct_types[itype](arg):
                    raise CommandInputError('Invalid value type: {}\n Expected {}'.format(arg, itype), func,)
                arg_length = len(arg)/2
                if (length != 0) and (strict and arg_length != length) or arg_length > length:
                    raise CommandInputError('Invalid bytes length: {} (len {} expected for `{}`)'.format(
                        arg_length,
                        length,
                        func.__name__,), func,)
            # transform input_data to be passed to a generic func
            nstrip_args = [int(arg, 16,) for arg in strip_args]
            bstrip_args = [arg.to_bytes(length, 'big',) for arg in nstrip_args]
            # call the function and print it response
            res = func(*bstrip_args)
            print(res, end='')
            # do not return any arguments
        return func_wrapper
    return wrapper
