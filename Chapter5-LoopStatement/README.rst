Loop Statement
==============

Normal program runs sequentially, Loop Statement makes the code block run
repeatedly.

.. image:: /images/loop.png

In Python, we use ``for`` or ``while`` to build loop statement, and use
``continue``, ``break`` to control it.

``continue`` is used to stop the current loop and start from the next.

.. image:: /images/loop_continue.png

``break`` is used to stop the whole loop.

.. image:: /images/loop_break.png

For-Loop
--------

For-loop is like traversal in Python. Syntax is like:

.. code-block:: python

    for iter_item in iterable_sequence:
        ...

It's actually a traversal of an iterable sequence like list, str, etc. That
brings giant convenience, which means we don't need to get elements from
their indices. If you are familiar with some other programming languages,
you probably do for-loop like:

.. code-block:: python

    animals = ['dog', 'cat', 'elephant', 'tiger', 'lion']
    for index in range(len(animals)):
        print(animals[index])

It's not wrong but there is an easier and more pythonic way:

.. code-block:: python

    for animal in animals:
        print(animal)

They print the same results:

.. code-block:: text

    dog
    cat
    elephant
    tiger
    lion

You are able to get the element from the sequence one by one easily.



While-Loop
----------
