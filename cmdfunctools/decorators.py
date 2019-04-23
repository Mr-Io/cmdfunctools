# -*- coding: utf-8 -*-
"""
cmdfunctools.decorators
~~~~~~~~~~~~~~~~~~~~~~~

Module with the decorators definitions to make function usable from command line.
"""
import functools
import sys

from .types import dct_type_check, dct_convert_from, dct_convert_to, default_arg, default_true
from .exceptions import CommandInputError


# decorator for transforming python functions in command line usable commands
def command_func(itype: str = '', otype: str = '', length: int = 0, strict_len: bool = True,):
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
                    raise CommandInputError('Received {} arguments ({} argument(s) expected for `{}`)'.format(
                        len(sys.argv)-1, n_args, func.__name__),
                        func,)
                input_args = sys.argv[1:]
            else:
                input_args = sys.stdin.readlines()
            strip_args = [arg.strip() for arg in input_args]
            for arg in strip_args:
                # Raise command input exceptions if incorrect type
                if not dct_type_check.get(itype, default_true)(arg):
                    raise CommandInputError('Invalid value type: {} ("{}" expected for `{}`)'.format(
                        arg, itype, func.__name__),
                        func,)
                arg_length = len(arg)
                if (length != 0) and ((strict_len and arg_length != length) or arg_length > length):
                    raise CommandInputError('Invalid bytes length: {} (len {} expected for `{}`)'.format(
                        arg_length,
                        length,
                        func.__name__,), func,)
            # transform input_data to be passed to a generic func
            istrip_args = [dct_convert_from.get(itype, default_arg)(arg, length=length)
                           for arg in strip_args]
            ostrip_args = [dct_convert_to.get(otype, default_arg)(arg) for arg in istrip_args]
            # call the function and print it response
            res = func(*ostrip_args)
            print(res, end='')
            # do not return any arguments
        return func_wrapper
    return wrapper
