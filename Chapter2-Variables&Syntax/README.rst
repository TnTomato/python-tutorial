Variables and Syntax
====================

Variable Types
--------------

Python has 6 basic variable types:

    Number_

    String_

    List_

    Dictionary_

    Tuple

    Set

Among these:

    Mutable: List, Dictionary

    Immutable: Number, String, Tuple

Python is a dynamically typed language. You don't need to declare type when
creating a variable. Just do like:

.. code-block:: python

    foo = 10
    bar = 'Sam'

.. _Number: https://github.com/openpyer/python-tutorial/tree/master/Chapter2-Variables%26Syntax#number
.. _String: https://github.com/openpyer/python-tutorial/tree/master/Chapter2-Variables%26Syntax#string
.. _List: https://github.com/openpyer/python-tutorial/tree/master/Chapter2-Variables%26Syntax#list
.. _Dictionary: https://github.com/openpyer/python-tutorial/tree/master/Chapter2-Variables%26Syntax#dictionary

Number
^^^^^^

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

    20.5 <class 'float'>

String
^^^^^^

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
    sentence6 = '''Hello every one. Nice to meet all of you. My name is Sam
     and I am 25 years old. I am a software engineer.'''
    # or
    sentence7 = """Hello every one. Nice to meet all of you. My name is Sam
     and I am 25 years old. I am a software engineer."""

Remember that single quotes act the same as double quotes. But usually, we
make a standard to reach a consensus in a specific project.

List
^^^^

A list is kind of like an array. It packages elements in square brackets([]).
Elements can be any type.

.. code-block:: python

    animals = ['dog', 'cat', 'tiger', 'wolf', 'rabbit']
    numbers = [111, 222, 333, 444, 555]

List can do indexing and slicing.

Using ``list[index]`` to index element.

Using ``list[start:end:step]`` to slice element. It can slice a list from
the start index value to the end index value(end index value excluded) with
the given step.

String and Tuple support the above operations too.

For example:

.. code-block:: python

    print(animals[0])  # The first element
    print(animals[:2])  # The first to the index value 2 element slice, but index value 2 element is excluded
    print(animals[2:])  # The index value 2 to the last element slice
    print(animals[2:-1])  # The index value 2 to the last element slice, but the last element is excluded
    print(animals[2:4])  # The index value 2 to the index value 4 element slice, but the index value 4 element is excluded
    print(animals[:])  # The first to the last element slice(copy the list)

Output:

.. code-block:: text

    dog
    ['dog', 'cat']
    ['tiger', 'wolf', 'rabbit']
    ['tiger', 'wolf']
    ['dog', 'cat', 'tiger', 'wolf', 'rabbit']

Dictionary
^^^^^^^^^^

A Python dictionary looks like a JSON.

.. code-block:: python

    sam = {
        'name': 'Sam',
        'age': 20,
        'hobbies': ['basketball', 'pcgames'],
        'pets': [
            {
                'type': 'dog',
                'name': 'Bob',
                'age': 2,
            },
            {
                'type': 'cat',
                'name': 'Alice',
                'age': 1
            }
        ]
    }

Two ways to get values from a dictionary.

``dict[key]`` can get value if the key exists, or raise a KeyError.

``dict.get(key)`` can get value if the key exists, or return a default value(default to ``None``)

For example:

.. code-block:: python

    print(sam['name'])
    print(sam.get('age'))
    print(sam['pets'][0]['type'])
    print(sam.get('gender'))

Output:

.. code-block:: text

    Sam
    20
    dog
    None

Python Keywords
---------------
Here is a way to list all of the Python Keywords:

>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

There are 35 keywords in total, which means you cannot name variables or
functions or classes after them. It's not necessary to remember all these
keywords. You will be familiar with them after coding for a period of time.

Python Syntax Intro
-------------------

Python uses 4 spaces as a single indent. These indents are the only controller
of your code blocks. Python, is not like other programming languages, doesn't
use ``{}`` to pack functions and classes.

TODO: 缩进 空格 换行