Operators
=========

You may have already seen some of the operators in the previous chapters. For
example: **1 + 2 = 3**. In this case, **+** and **=** are called operators.

In Python, the operators below are supported.

    - `Arithmetic Operators`_
    - `Assignment Operators`_

Please learn with the examples: `examples.py`_

.. _Arithmetic Operators:https://github.com/openpyer/python-tutorial/tree/master/Chapter3-Operators#arithmetic-operators
.. _Assignment Operators: https://github.com/openpyer/python-tutorial/tree/master/Chapter3-Operators#assignment-operators
.. _examples.py: https://github.com/openpyer/python-tutorial/blob/master/Chapter3-Operators/examples.py

Arithmetic Operators
--------------------

+---------+---------------------------------------------------------------+------------------+--------+
|Operator |Description                                                    |Example           | Output |
+=========+===============================================================+==================+========+
|\+       |- positive number                                              |- \+3             |- 3     |
|         |- add two objects                                              |- 1 + 2           |- 3     |
+---------+---------------------------------------------------------------+------------------+--------+
|\-       |- negative number                                              |- \-3             |- -3    |
|         |- subtract two objects                                         |- 2 - 1           |- 1     |
+---------+---------------------------------------------------------------+------------------+--------+
|\*       |- multiply two objects                                         |- 3 * 2           |- 6     |
|         |- sequences can also be multiplied by int                      |- 'a' * 3         |- 'aaa' |
+---------+---------------------------------------------------------------+------------------+--------+
|\/       |one object is divided by another, avoid any division by zero   |4 / 2             |2.0     |
+---------+---------------------------------------------------------------+------------------+--------+
|\**      |exponentiation                                                 |2 ** 10           | 1024   |
+---------+---------------------------------------------------------------+------------------+--------+
|//       |round down the result of division                              |- 5 // 2          |- 2     |
|         |                                                               |- -9 // 2         |- -3    |
+---------+---------------------------------------------------------------+------------------+--------+
|%        |get the remainder of division                                  |5 % 2             |1       |
+---------+---------------------------------------------------------------+------------------+--------+

Code examples:

.. code-block:: python

    a = 10
    b = 3

    print('a + b =', a + b)
    print('a - b =', a - b)
    print('a * b =', a * b)
    print('a / b =', a / b)
    print('a ** b =', a ** b)
    print('a // b =', a // b)
    print('a % b =', a % b)

Outputs:

.. code-block:: text

    a + b = 13
    a - b = 7
    a * b = 30
    a / b = 3.3333333333333335
    a ** b = 1000
    a // b = 3
    a % b = 1

Assignment Operators
--------------------

