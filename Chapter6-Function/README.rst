Function
========

When you code more and more, and you find it a little bit hard to manage
your codes. Try *functional programming*.

In short, *functional programming* makes program structured. We just take
a piece of code as a function. Then pack them inside a function. Functions
make it easier to reuse a same piece of code. Like the built-in function
``print()``. We can build functions ourselves.

A function is like:

.. code-block:: python

    def function_name(parameter1, parameter2):
        """(docstring)explanations to the function
        multi lines
        """
        ...
        return something

1. Use ``def`` as a start of a function.
2. Define function's name after a whitespace.
3. Use a pair of parentheses to define parameters.
4. Add a colon at the end of the line.
5. Define docstrings after an indent at the next line.
6. Finish your code block.
7. Return something(A function can return nothing, just omit ``return``. It acts like ``return None``).

It's the normal way to define a function. But I recommend you to do like this:

.. code-block:: python

    def function_name(parameter: type) -> type:
        """
        docstring
        :param parameter: explanation to the parameter
        """
        ...
        return something

..
    TODO: hyperlink to Python's typing.

As we know, Python is a weak typed programming language. Using *type hint*
helps indicate the types of parameters and returned values. There is a module
called ``typing`` which plays a powerful role in type hinting. See the example
first and I will explain it in a future chapter.

.. code-block:: python

    from typing import List


    def convert_to_str(sequence: List[int]) -> List[str]:
        """Convert any `int` object to `str` in a given sequence

        :param sequence: a sequence to be converted.
        """
        converted = []
        for i in sequence:
            converted.append(str(i))
        return converted

Then we can call the function after it.

.. code-block:: python

    to_be_converted = [1, 2, 3, 4, 5]
    print(convert_to_str(to_be_converted))

Output:

.. code-block:: text

    ['1', '2', '3', '4', '5']

Parameter
=========

Function accepts several kind of parameters.

    - Positional Parameter

    - Default Parameter

    - Changeable Parameter

    - Keyword Parameter

    - Named Keyword Parameter

    - Positional-Only Parameters

Positional Parameter
--------------------

Let's start from an example. Let's define a function to double a int number:

.. code-block:: python

    def double(number: int) -> int:
        return number * 2

When ``double`` is called, only one parameter ``number`` is passed.

.. code-block:: python

    print(double(5))  # 10
    print(double(10))  # 20

What if we want to double a number for several times?

.. code-block:: python

    print(double(double(double(5))))  # 40

It can't go wrong. But why don't think about a much more simple one? We can
define a function like:

.. code-block:: python

    def double(number: int, times: int) -> int:
        for _ in range(times):
            number *= 2
        return number

hint: ``_`` means you don't need to use the iter object in the for-loop.

Then you can double a number any times:

.. code-block:: python

    print(double(5, 3))  # 40
    print(double(7, 20))  # 7340032

This is called *Positional Parameter*. They must be passed one by one in order.

Default Parameter
-----------------

Let's continue from the previous example. When we want to double 5 just like
at the beginning, we cannot do like ``double(5)``. A TypeError will be raised:

.. code-block:: text

    TypeError: double() missing 1 required positional argument: 'times'

Obviously, we want to do a double at 5 using ``double(5)``, but how? That is
what *Default Parameter* do. Our purpose is clear: when parameter ``times``
equals 1, we want to omit this parameter when the function is called. We just
define like:

.. code-block:: python

    def double(number: int, times: int = 1) -> int:
        for _ in range(times):
            number *= 2
        return number

Then it works, they means the same:

.. code-block:: python

    print(double(5))  # 10
    print(double(5, 1))  # 10

It's worth noting that, *default parameters* must be after *optional parameters*.
Otherwise, a SyntaxError will be raised.

.. code-block:: python

    def double(times: int = 1, number: int) -> int:
        ...

Output:

.. code-block:: text

    SyntaxError: non-default argument follows default argument

Another important point: Mutable objects cannot act like default arguments.

.. code-block:: python

    def append_one(sequence=[]):
        sequence.append(1)
        return sequence

You will see:

.. code-block:: python

    print(append_one())  # [1]
    print(append_one())  # [1, 1]
    print(append_one())  # [1, 1, 1]

See where is the problem? Let's do some improvement:

.. code-block:: python

    def append_one(sequence=None):
        if sequence is None:
            sequence = []
        sequence.append(1)
        return sequence

Then it goes right:

.. code-block:: python

    print(append_one())  # [1]
    print(append_one())  # [1]
    print(append_one())  # [1]

Changeable Parameter
--------------------

Also start from an example. We want a function to sum serveral integers,
usually we do like:

.. code-block:: python

    def add_all(numbers: list) -> int:
        result = 0
        for number in numbers:
            result += number
        return result

Then we must build a list first.

.. code-block:: python

    print(add_all([1, 2, 3, 4]))  # 10
    print(add_all([10, 20, 30]))  # 60

When we want the function accept a sequence, but not a list passed. We can:

.. code-block:: python

    def add_all(*args) -> int:
        result = 0
        for number in args:
            result += number
        return result

Then call the function like:

.. code-block:: python

    print(add_all(1, 2, 3, 4))  # 10
    print(add_all(10, 20, 30))  # 60

``*args`` turns several parameters into a Python tuple.

.. code-block:: python

    def add_all(*args):
        print(args)


    add_all(1, 2, 3)  # (1, 2, 3)

You can pass any number of parameters.

.. code-block:: python

    print(add_all(1, 2, 3))  # 6
    print(add_all())  # 0

If there is a ready list ``numbers = [1, 2, 3, 4]``, we don't need to pass the
elements one by one like:

.. code-block:: python

    print(add_all(numbers[0], numbers[1], numbers[2], numbers[3]))  # 10

It's not wrong but needless. We can put an asterisk(*) before ``numbers`` to
change the elements to changeable parameters.

.. code-block:: python

    print(add_all(*numbers))  # 10

Keyword Parameter
-----------------

*Keyword Parameter* turns several ``key=value`` type parameters into a
Python dictionary.

.. code-block:: python

    def introduce(name, age, **kwargs):
        print('name:', name, 'age:', age, 'extra:', kwargs)

``**kwargs`` accept several optional parameters, we can do like:

.. code-block:: python

    introduce('Sam', 20, skill='Python', job='web')

Output:

.. code-block:: text

    name: Sam age: 20 extra: {'skill': 'Python', 'job': 'web'}

Similar to *Changeable Parameter*, we can turn a Python dictionary into
*Keyword Parameter*.

.. code-block:: python

    extra = {
        'skill': 'Python',
        'job': 'web',
        'hobbies': ['pc-games', 'basketball']
    }
    introduce('Sam', 20, **extra)

Output:

.. code-block:: text

    name: Sam age: 20 extra: {'skill': 'Python', 'job': 'web', 'hobbies': ['pc-games', 'basketball']}

Named Keyword Parameter
-----------------------

There is no limit of *Keyword Parameter*, which means you can pass any
key-value you want. But how to set a limitation? We want to check if
``skill`` and ``job`` is passed as keyword parameters.

.. code-block:: python

    def introduce(name, age, **kwargs):
        if 'skill' not in kwargs:
            ...
        if 'job' not in kwargs:
            ...
        print('name:', name, 'age:', age, 'extra:', kwargs)

But other parameters still can be passed without limitation. If we just want
``skill`` and ``job`` the only two keyword parameters, we should use
*Named Keyword Parameter*.

.. code-block:: python

    def introduce(name, age, *, skill, job):
        print('name:', name, 'age:', age, 'skill:', skill, 'job': job)


    introduce('Sam', 20, skill='Python', job='web')

Output:

.. code-block:: text

    name: Sam age: 20 skill: Python job: web

We use an asterisk(*) to split positional parameters and named keyword
parameters.

If there is a *Changeable Parameter*, you don't need to put an asterisk(*).

.. code-block:: python

    def introduce(name, age, *args, skill, job):
        ...

After all, you have learned how to define any function you like.

Let's do some exercises, see it in `exercise.py`_ and check `answer.py`_
yourself.

.. _`exercise.py`: https://github.com/TnTomato/python-tutorial/blob/master/Chapter6-Function/exercise.py
.. _`answer.py`: https://github.com/TnTomato/python-tutorial/blob/master/Chapter6-Function/answer.py
