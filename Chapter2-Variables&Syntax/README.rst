Variables and Syntax
====================

Variable Types
--------------

Python has 6 basic variable types: Number_, String_, List, Dictionary, Tuple
and Set.

Mutable: List, Dictionary

Immutable: Number, String, Tuple

Python is a dynamically typed language. You don't need to declare type when
creating a variable. Just do like:

.. code-block:: python

    foo = 10
    bar = 'Sam'

.. _Number: https://github.com/openpyer/python-tutorial/tree/master/Chapter2-Variables%26Syntax#1number
.. _String: https://github.com/openpyer/python-tutorial/tree/master/Chapter2-Variables%26Syntax#2string

1.Number
^^^^^^^^

Number includes int, float, complex and bool.

.. code-block:: python

    # Python now has type hints, in order to indicate variable's type
    a: int = 10
    b: float = 10.5
    c: complex = 2 + 3j
    d: bool = True

You can try to do methematical operations using all variables above. Python
will do type conversion automatically for the result. For example:

.. code-block:: python

    result = a + b
    print(result, type(result))

The output is:

.. code-block:: text

    20.5 float

2.String
^^^^^^^^

Python use both single quotes(') and double quotes("). Both of the following
means the same.

.. code-block:: python

    sentence1 = "Nice to meet you."
    sentence2 = 'Nice to meet you.'

If you want to use quotes inside a String. You can do like:

.. code-block:: python

    sentence3 = "Sam said 'Nice to meet yuo' to John."
    # or
    sentence4 = 'Sam said \'Nice to meet yuo\' to John.'

But if your String variable is too long, you need to process like:

.. code-block:: python

    sentence5 = 'Hello every one. Nice to meet all of you. My name is Sam ' \
                'and I am 25 years old. I am a software engineer.'
    # or
    sentence4 = '''Hello every one. Nice to meet all of you. My name is Sam
     and I am 25 years old. I am a software engineer.'''
    # or
    sentence4 = """Hello every one. Nice to meet all of you. My name is Sam
     and I am 25 years old. I am a software engineer."""

Remember that single quotes act the same as double quotes. But usually, we
make a standard to reach a consensus in a specific project.

Python Keywords
---------------



Python Syntax Intro
-------------------

Python uses 4 spaces as a single indent. These indents are the only controller
of your code blocks. Python, is not like other programming languages, doesn't
use ``{}`` to pack functions and classes.

TODO: 缩进 空格 换行