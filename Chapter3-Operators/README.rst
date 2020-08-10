Operators
=========

You may have already seen some of the operators in the previous chapters. For
example: **1 + 2 = 3**. In this case, **+** and **=** are called operators.

In Python, the operators below are supported.

    - `Arithmetic Operators`_
    - `Assignment Operators`_
    - `Comparison Operators`_
    - `Logical Operators`_

Please learn with the examples: `examples.py`_

.. _Arithmetic Operators: https://github.com/TnTomato/python-tutorial/tree/master/Chapter3-Operators#arithmetic-operators
.. _Assignment Operators: https://github.com/TnTomato/python-tutorial/tree/master/Chapter3-Operators#assignment-operators
.. _Comparison Operators: https://github.com/TnTomato/python-tutorial/tree/master/Chapter3-Operators#comparison-operators
.. _Logical Operators: https://github.com/TnTomato/python-tutorial/tree/master/Chapter3-Operators#logical-operators
.. _examples.py: https://github.com/TnTomato/python-tutorial/blob/master/Chapter3-Operators/examples.py

Arithmetic Operators
--------------------

+---------+----------------------------------------------------------------+------------------+--------+
|Operator |Description                                                     |Example           | Output |
+=========+================================================================+==================+========+
|\+       |- positive number                                               |- \+3             |- 3     |
|         |- add two objects                                               |- 1 + 2           |- 3     |
+---------+----------------------------------------------------------------+------------------+--------+
|\-       |- negative number                                               |- \-3             |- -3    |
|         |- subtract two objects                                          |- 2 - 1           |- 1     |
+---------+----------------------------------------------------------------+------------------+--------+
|\*       |- multiply two objects                                          |- 3 * 2           |- 6     |
|         |- sequences can also be multiplied by int                       |- 'a' * 3         |- 'aaa' |
+---------+----------------------------------------------------------------+------------------+--------+
|\/       |- one object is divided by another                              |- 4 / 2           |- 2.0   |
|         |- avoid any division by zero                                    |- 4 / 0           |- Error |
+---------+----------------------------------------------------------------+------------------+--------+
|\**      |- exponentiation                                                |- 2 ** 10         |- 1024  |
+---------+----------------------------------------------------------------+------------------+--------+
|//       |- round down the result of division                             |- 5 // 2          |- 2     |
|         |                                                                |- -9 // 2         |- -3    |
+---------+----------------------------------------------------------------+------------------+--------+
|%        |- get the remainder of division                                 |- 5 % 2           |- 1     |
+---------+----------------------------------------------------------------+------------------+--------+

Code examples:

.. code-block:: python

    a = 10
    b = 5

    print('a + b =', a + b)
    print('a - b =', a - b)
    print('a * b =', a * b)
    print('a / b =', a / b)
    print('a ** b =', a ** b)
    print('a // b =', a // b)
    print('a % b =', a % b)

Output:

.. code-block:: text

    a + b = 15
    a - b = 5
    a * b = 50
    a / b = 2.0
    a ** b = 100000
    a // b = 2
    a % b = 0

Assignment Operators
--------------------

You must be very familiar with ``=``. But have you seen ``+=``, ``-=``, ``*=``?
It will be easier to understand the rest of the **Assignment Operators** when
you know how ``+=`` works. All the rest are similar. Now take a look at the
table:

+---------+------------------------------------+-----------------------------------------+
|Operator |Description                         |Example and Explanation                  |
+=========+====================================+=========================================+
|=        |- assign values to variables        |- a = 2, let ``a`` equals ``2``          |
+---------+------------------------------------+-----------------------------------------+
|+=       |- assign the sum of the variable    |- a += 2, the same as ``a = a + 2``      |
|         |  and the value onthe right to the  |                                         |
|         |  variable itself                   |                                         |
+---------+------------------------------------+-----------------------------------------+
|-=       |- assign the difference of the      |- a -= 2, the same as ``a = a - 2``      |
|         |  variable and the value on the     |                                         |
|         |  right to the variable itself      |                                         |
+---------+------------------------------------+-----------------------------------------+
|\*=      |- assign the product of the         |- a \*= 2, the same as ``a = a * 2``     |
|         |  variable and the value on the     |                                         |
|         |  right to the variable itself      |                                         |
+---------+------------------------------------+-----------------------------------------+
|/=       |- assign the result of dividing the |- a /= 2, the same as ``a = a / 2``      |
|         |  variable and the value on the     |                                         |
|         |  right to the variable itself      |                                         |
+---------+------------------------------------+-----------------------------------------+
|\**=     |- assign the result of              |- a \**= 2, the same as ``a = a \** 2``  |
|         |  exponentiation to the variable    |                                         |
|         |  itself                            |                                         |
+---------+------------------------------------+-----------------------------------------+
|//=      |- assign the result(after rounded   |- a //= 2, the same as ``a = a // 2``    |
|         |  down) of dividing the variable    |                                         |
|         |  and the value on the right to the |                                         |
|         |  variable itself                   |                                         |
+---------+------------------------------------+-----------------------------------------+
|%=       |- assign the remainder of dividing  |- a %= 2, the same as ``a = a % 2``      |
|         |  the variable and the value on the |                                         |
|         |  right to the variable itself      |                                         |
+---------+------------------------------------+-----------------------------------------+

Obviously, ``equal sign after an arithmetic operator`` means do the assignment
after the arithmetic operation. Let's see some code examples:

.. code-block:: python

    # Let us assign `c`, `d`, `e`, `f`, `g`, `h`, `i` all to 10
    # In python, we assign the same value to multiple variables like this
    c = d = e = f = g = h = i = 10

    c += 2
    print('c += 2, c is', c)

    d -= 2
    print('d -= 2, d is', d)

    e *= 2
    print('e *= 2, e is', e)

    f /= 2
    print('f /= 2, f is', f)

    g **= 2
    print('g **= 2, g is', g)

    h //= 2
    print('h //= 2, h is', h)

    i %= 2
    print('i %= 2, i is', i)

Output:

.. code-block:: text

    c += 2, c is 12
    d -= 2, d is 8
    e *= 2, e is 20
    f /= 2, f is 5.0
    g **= 2, g is 100
    h //= 2, h is 5
    i %= 2, i is 0

Comparison Operators
====================

Comparison operators usually used in conditional statement. They do like 'more
than', 'less than' or something. See what are they:

+---------+------------------------------------------------------+-------------------+----------+
|Operator |Description                                           |Example            | Return   |
+=========+======================================================+===================+==========+
|==       |- determine whether one object is equal to another    |- 2 == 2           |- True    |
|         |                                                      |- 1 == 2           |- False   |
+---------+------------------------------------------------------+-------------------+----------+
|!=       |- determine whether one object is not equal to        |- 1 != 2           |- True    |
|         |  another                                             |- 2 != 2           |- False   |
+---------+------------------------------------------------------+-------------------+----------+
|>        |- determine whether one object is greater than        |- 2 > 1            |- True    |
|         |  another                                             |- 2 > 2            |- False   |
+---------+------------------------------------------------------+-------------------+----------+
|<        |- determine whether one object is less than another   |- 1 < 2            |- True    |
|         |                                                      |- 2 < 2            |- False   |
+---------+------------------------------------------------------+-------------------+----------+
|>=       |- determine whether one object is greater than or     |- 2 >= 1           |- True    |
|         |  equal to another                                    |- 2 >= 2           |- True    |
|         |                                                      |- 1 >= 2           |- False   |
+---------+------------------------------------------------------+-------------------+----------+
|<=       |- determine whether one object is less than or equal  |- 1 <= 2           |- True    |
|         |  to another                                          |- 2 <= 2           |- True    |
|         |                                                      |- 2 <= 1           |- False   |
+---------+------------------------------------------------------+-------------------+----------+

There is also a comparion operator ``<>`` in Python 2, but this is a Python 3
tutorial, you know.

Oops, no examples here. It's actually too simple, you know.

Oops again, why the three types of operators have the same number of letters?
'Arithmetic' has 10 letters, 'Assignment' has 10 letters, 'Comparison' has 10
letters! I have no idea, that's what the dictionary told me :-)

Sorry for my poor English.

Whatever, the next one is not!

Logical Operators
=================

As we have learned before, ``bool`` is inherited from ``int``. So ``True``
also equals 1, ``False`` equals 0. It can help you understand the logical
operators easier.

+---------+---------------------------+-------------------+----------+
|Operator |Description                |Example            | Return   |
+=========+===========================+===================+==========+
|and      |- Boolean 'AND'            |- 1 and 2          |- 2       |
|         |                           |- 2 and 1          |- 1       |
|         |                           |- 0 and 1          |- 0       |
|         |                           |- 1 and 0          |- 0       |
+---------+---------------------------+-------------------+----------+
|or       |- Boolean 'OR'             |- 1 or 2           |- 1       |
|         |                           |- 2 or 1           |- 2       |
|         |                           |- 0 or 1           |- 1       |
|         |                           |- 1 or 0           |- 1       |
+---------+---------------------------+-------------------+----------+
|not      |- Boolean 'NOT', reverse   |- not True         |- False   |
|         |  the boolean result       |- not 1 == 1       |- False   |
+---------+---------------------------+-------------------+----------+

No examples too.

Member Operators
================

+---------+-------------------------------------------------------------------+
|Operator |Description                                                        |
+=========+===================================================================+
|in       |- Judge whether an object is inside a sequence, the opposite one   |
|         |  is ``not in``                                                    |
+---------+-------------------------------------------------------------------+

Code examples:

.. code-block:: python

    j = 30
    numbers = [10, 20, 30, 40, 50]

    if j in numbers:
        print('`j` is in `numbers`')
    else:
        print('`j` is not in `numbers`')


Output:

.. code-block:: text

    `j` is in `numbers`

Identity Operations
===================

+---------+-------------------------------------------------------------------+
|Operator |Description                                                        |
+=========+===================================================================+
|is       |- Judge whether two objects share the same memory address, the     |
|         |  opposite one is ``is not``                                       |
+---------+-------------------------------------------------------------------+

Code examples:

.. code-block:: python

    k = [1, 2, 3]
    m = n = [1, 2, 3]

    print(m is n)
    print(k is n)

Output:

.. code-block:: text

    True
    False

Bitwise Operators
=================

bitwise-and
bitwise-or
...