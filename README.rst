..  The Readme should be the single most important document in your codebase; writing it first is the proper thing to do.
    * screenshots logo/demo etc..
    * api reference (documentation)
    * how to contribute to it and credits

Cmdfunctools: command line tools from python functions
======================================================
|Version| |License| |Python| |Contributors|

.. |Version| image:: https://img.shields.io/pypi/v/cmdfunctools.svg
    :target: https://pypi.org/project/cmdfunctools/

.. |License| image:: https://img.shields.io/github/license/Mr-Io/cmdfunctools.svg
    :target: https://pypi.org/project/cmdfunctools/

.. |Python| image:: https://img.shields.io/pypi/pyversions/cmdfunctools.svg
    :target: https://pypi.org/project/cmdfunctools/

.. |Contributors| image:: https://img.shields.io/github/contributors-anon/Mr-Io/cmdfunctools.svg
    :target: https://pypi.org/project/cmdfunctools/

When developing a new package, there are python functions that
you want to make also available from the command line.
To do so, an additional function is needed; a specially designed command-line-function
which is then referenced in the setup.py file, inside the `entry_points` key.
This command-line-function is special indeed, since
it cannot have arguments (it uses instead `sys.stdin` or `sys.argv` as inputs) and
cannot have return values (it uses instead `print()` as output).

**With cmdfunctools you can automatically create a command-line-function from any python function.**

Installation
------------
The source code can be downloaded from GitHub, where the code is `always available`_.

It can also be installed from PyPI running::

    $ pip install cmdfunctools


Usage
-----
To create a command-line-function use the `comand_func` decorator::

    from cmdfunctools import command_func

    @command_func(itype='int', otype='int')
    def add(a, b)
        res = a + b
        return res

Now the function can be referenced **as is** in `entry_points` inside setup.py and,
after the package installation, it can be used from the command line interface::

    $ add 3 2
    5

The original function can still be used within python code using the __wrapped__() method::

    >>> add.__wrapped__(3, 2)
    5

Features
--------
* Automatic number of arguments check
* Automatic argument type check
* Optional argument length check (equal or less-or-equal)
* Pipelines supported
* I/O argument types supported:

    * integer
    * hexadecimal

**The project is in** `3-Alpha`_ **development status, new features will be added before 5-Production/Stable.**

.. _`always available`: https://github.com/Mr-Io/cmdfunctools.git
.. _`3-Alpha`: https://pypi.org/project/cmdfunctools/
