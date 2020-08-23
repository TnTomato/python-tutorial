Conditional Statement
=====================

Since this chapter, we will have some exercises after class.

Life is full of conditions. You go to school at a proper age, you buy a car
when you have enough money, you go to college only if you pass the exam, etc.
Each situation has its precondtion. If you learn hard, you succeed.

How to express conditions in Python? Let's start from an example:

.. code-block:: python

    if age < 18:
        print('not adult')
    else:
        print('adult')

It prints ``not adult`` when age is less then 18, otherwise, it prints
``adult``.

What about multi-conditions:

.. code-block:: python

    if age < 18:
        print('not adult')
    elif 18 <= age < 60:
        print('adult')
    else:
        print('old')

``elif`` statement is for multi-conditions. There can be several ``elif`` to
show a variety of conditions.

Additional, Python takes non-zero, non-null, non-empty object for ``True``,
and zero, null, empty object for ``False``.

.. code-block:: python

    foo = 0  # False
    bar = 1  # True
    cris = None  # False
    eric = []  # False
    george = ['item']  # True

    # So you can easily code
    if not cris:
        print('cris is empty')
    else:
        print('cris is not empty')

Let's pay particular attention to a special one. When you mean to judge if a
list is empty or not, you don't need to judge it's length like:

.. code-block:: python

    a = []
    if len(a) == 0:
        print('a is empty')
    else:
        print('a is not empty')

There is an simpler expression:

.. code-block:: python

    a = []
    if not a:
        print('a is empty')
    else:
        print('a is not empty')

It's the same as Python dictionary and other similar objects.

Exercises
---------

Just finish `exercise.py`_ and run. If it's result is correct, you pass
this chapter.

`answer.py`_ show the reference answer.

.. _`exercise.py`: https://github.com/TnTomato/python-tutorial/blob/master/chapters/Chapter4-ConditionalStatement/exercise.py
.. _`answer.py`: https://github.com/TnTomato/python-tutorial/blob/master/chapters/Chapter4-ConditionalStatement/answer.py
