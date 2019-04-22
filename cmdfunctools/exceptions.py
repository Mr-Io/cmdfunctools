# -*- coding: utf-8 -*-
"""
cmdfunctools.exceptions
~~~~~~~~~~~~~~~~~~~~~

This module contain the set of cmdfunctools's exceptions.
"""


class CmdfunctoolsBaseError(Exception):
    """There was an ambiguous exception that occurred while handling agrobits."""


class CommandInputError(CmdfunctoolsBaseError):
    """A command input error occurred."""
    def __init__(self, msg: str, func):
        CmdfunctoolsBaseError.__init__(self, msg + '\n' + func.__doc__)
        self.func = func
