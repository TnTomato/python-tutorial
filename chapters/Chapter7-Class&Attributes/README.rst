Class
=====

After you have learned how to define a function, you may think you've probably
got all the programming skills. Definitely not! Have you ever heard of
*Object-oriented Programming*?

We've already used a word *object* several times in the previous chapters. Do
you really know what an object is? Follow me and I will tell the answer.

The key of *Object-oriented Programming* is *class*. An object is an
*instance* from a *class*. A class is like an abstract conception. Any instance
is created from some class. We call them *object*. They have the same *methods*
but different *attributes*. For example, let's see how to define a class:

.. code-block:: python

    class Animal(object):
        ...

We define a *Camel Case* name after a keyword ``class``. What in the
parentheses is the class's *parent class*. The ``object`` is the parent class
of all Python classes. To be pythonic, all classes should explicitly inherit
from ``object``.

..
    参考https://www.liaoxuefeng.com/wiki/1016959663602400/1017496031185408
    实例化
    类属性，__init__方法
    提一下魔术方法
