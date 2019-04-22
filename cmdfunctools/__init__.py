# -*- coding: utf-8 -*-
"""
cmdfunctools
~~~~~~~~~~~~

cmdfunctools package.
"""

from .__version__ import (__author__, __version__, __author_email__, __copyright__, __description__, __license__,
                          __title__, __url__)

from .decorators import command_func

from .exceptions import CmdfunctoolsBaseError, CommandInputError
