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
7. Return something(A function can return nothing, just omit ``return``. It
acts like ``return None``).

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

TODO: Several kind of parameters