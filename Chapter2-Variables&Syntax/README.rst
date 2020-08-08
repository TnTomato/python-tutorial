Variables and Syntax
====================

Welcome to Chapter 2. This chapter contains 4 main themes. Click and skip to
the target theme.

    `Variable Naming`_

    `Variable Types`_

    `Python Keywords`_

    `Python Syntax`_

.. _Variable Naming: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#variable-naming
.. _Variable Types: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#variable-types
.. _Variable Keywords: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#python-keywords
.. _Variable Syntax: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#python-syntax

Variable Naming
----------------

Variable naming is a serious issue. A thousand programmers may have a thousand
ways to name a variable.

In Python, we usually name variables following the rule of ``snake case``.
For example:

.. code-block:: python

    file_name = 'main.py'
    people_in_allowed_list = ['Tom', 'Jerry']

These are not recommended:

.. code-block:: python

    fileName = 'main.py'
    PeopleInAllowedList = ['Tom', 'Jerry']

Variable Types
--------------

Python has 6 basic variable types:

    Number_

    String_

    List_

    Dictionary_

    Tuple_

    Set_

Among these:

    Mutable: List, Dictionary

    Immutable: Number, String, Tuple

Python is a dynamically typed language. You don't need to declare type when
creating a variable. Just do like:

.. code-block:: python

    foo = 10
    bar = 'Sam'

.. _Number: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#number
.. _String: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#string
.. _List: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#list
.. _Dictionary: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#dictionary
.. _Tuple: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#tuple
.. _Set: https://github.com/TnTomato/python-tutorial/tree/master/Chapter2-Variables%26Syntax#set

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

Output:

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

Two ways to get values from a dictionary:

``dict[key]`` can get value if the key exists, or raise a KeyError.

``dict.get(key)`` can get value if the key exists, or return a default value(default to ``None``)

For example:

.. code-block:: python

    print(sam['name'])
    print(sam.get('age'))
    print(sam['pets'][0]['type'])
    print(sam.get('gender'))
    print(sam.get('mood'), 'happy')

Output:

.. code-block:: text

    Sam
    20
    dog
    None
    happy

Tuple
^^^^^

If it's said that a list seems like an array, then a tuple would be like
kind of a structure. The biggest difference between list and tuple is that
list is **mutable**, but tuple is **immutable**.

In general, list usually contains **homogenous data**, but tuple usually
contains **heterogeneous data**.

About how to create a tuple:

.. code-block:: python

    john = ('john', 20, 180)
    lily = 'lily', 19, 168
    tmp = (1, )

Remember to put a comma after the only element.

A function with more than one returned value returns a tuple. For example:

.. code-block:: python

    # This is a function to get `name` and `age` from a given dictionary
    def get_meta(info: dict) -> Tuple[str, int]:
        name = info.get('name')
        age = info.get('age')
        return name, age


    sam_meta = get_meta(sam)
    print(sam_meta, isinstance(sam_meta, tuple))

Output:

.. code-block:: text

    ('Sam', 20)
    True

Don't worry if you don't know the meaning of the above code. There
will be a detailed introduction of **function** later.

Set
^^^

Set is an unordered, distinct sequence. We use ``{}`` or ``set()`` to create
sets.

.. code-block:: python

    fruits = {'apple', 'orange', 'pineapple', 'cherry'}

Attention: You create an empty set from ``set()`` instead of ``{}`` because
``{}`` represents an empty dictionary.

Some of the basic operations of Set:

.. code-block:: python

    fruits.add('watermelon')  # add an element
    print(fruits)
    fruits.update(['pear', 'banana'])  # add several elements
    print(fruits)
    fruits.remove('apple')  # remove an element, raise an Exception if it's not exists
    print(fruits)
    fruits.pop()  # remove and return the first element after a random order
    print(fruits)

Output:

.. code-block:: text

    {'orange', 'apple', 'cherry', 'watermelon', 'pineapple'}
    {'banana', 'orange', 'apple', 'cherry', 'watermelon', 'pineapple', 'pear'}
    {'banana', 'orange', 'cherry', 'watermelon', 'pineapple', 'pear'}
    {'orange', 'cherry', 'watermelon', 'pineapple', 'pear'}

Python Keywords
---------------
Here is a way to list all of the Python Keywords:

>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

Also see in `keywords.py`_.

There are 35 keywords in total, which means you cannot name variables or
functions or classes after them. It's not necessary to remember all these
keywords. You will be familiar with them after coding for a period of time.

.. _keywords.py: https://github.com/TnTomato/python-tutorial/blob/master/Chapter2-Variables%26Syntax/keywords.py

Python Syntax
-------------

Python uses 4 spaces as a single indent. These indents are the only controller
of your code blocks. Python, is not like other programming languages, doesn't
need to pack code blocks with ``{}``.

Do you remember the function named ``get_meta`` inside `Tuple`_ above? That's
how Python do with code blocks. Wrong indents will raise an
``IndentationError``.

As a stadard, we always add spaces and empty lines somewhere to make our
codes elegant. Let's see a terrible one:

.. code-block:: python

    import time
    def pause(sec:int)->None:
        time.sleep(sec)
    def strange_add(a:int,b:int)->int:
        a+=10
        return a+b
    if __name__ == '__main__':
        print('start')
        result=strange_add(5,7)
        pause(2)
        print(result)
        print('end')

No doubt, this one is better:

.. code-block:: python

    import time


    def pause(sec: int) -> None:
        time.sleep(sec)


    def strange_add(a: int, b: int) -> int:
        a += 10
        return a + b


    if __name__ == '__main__':
        print('start')
        result = strange_add(5, 7)
        pause(2)
        print(result)
        print('end')

Also see in `syntax.py`_.

Be an elegant coder, because you will never code alone all your lifetime.
As ``Dave Carhart`` said, always code as if the guy who ends up maintaining,
or testing your code will be a violent psychopath who knows where you live.

.. _syntax.py: https://github.com/TnTomato/python-tutorial/blob/master/Chapter2-Variables%26Syntax/syntax.py