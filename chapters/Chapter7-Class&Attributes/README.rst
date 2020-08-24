Class
=====

After you have learned how to define a function, you may think you've probably
got all the programming skills. Definitely not! Have you ever heard of
*Object-oriented Programming*?

We've already used a word *object* several times in the previous chapters. Do
you really know what an object is? Follow me and I will tell the answer.

Definition
----------

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

Now you can declare an instance:

.. code-block:: python

    duck = Animal()
    fish = Animal()
    print(duck)
    print(fish)

Run it and the console shows:

.. code-block:: text

    <__main__.Animal object at 0x000002D81D108430>
    <__main__.Animal object at 0x000002D81D11EDF0>

Attribute
---------

You can define a class's attributes like:

.. code-block:: python

    class Animal(object):

        name: str = 'Booboo'
        age: int = 1

``name`` and ``age``, they are the same to all instances:

.. code-block:: python

    duck = Animal()
    fish = Animal()
    print(duck.name)  # Booboo
    print(duck.age)  # 1
    print(fish.name)  # Booboo
    print(fish.age)  # 1

But you can change the attribute's value on your own, then it will be different.
For example:

.. code-block:: python

    duck.name = 'Boo'
    fish.age = 2
    print(duck.name)  # Boo
    print(duck.age)  # 1
    print(fish.name)  # Booboo
    print(fish.age)  # 2

Method
------

Before we talk about class's method, see the code below:

.. code-block:: python

    class Animal(object):

        def __init__(self, name, age):
            self.name = name
            self.age = age

If you are familiar with *Java* or other programming language, you may take
this as a constructor. Indeed, it is. In Python, we use ``__init__``, a magic
method, to define some member variables. It's similar to function defining.
But remember ``self`` must stay at the first position of all paramters. The
``self`` means the class's instance. You can name it after anything you want,
but ``self`` is kind of an common agreement. ``__init__`` will be called
automatically when an instance is created.

This time we declare an instance like:

.. code-block:: python

    duck = Animal('Boo', 1)
    fish = Animal('Booboo', 2)

    print(duck.name)  # Boo
    print(duck.age)  # 1
    print(fish.name)  # Booboo
    print(fish.age)  # 2

Any other method can be defined and call it like:

.. code-block:: python

    class Animal(object):

        def __init__(self, name, age, sound):
            self.name = name
            self.age = age
            self.sound = sound

        def make_some_noise(self):
            print(self.sound)


    duck = Animal('Boo', 1, 'quack')
    fish = Animal('Booboo', 2, 'mute')

    duck.make_some_noise()  # quack
    fish.make_some_noise()  # mute

There are two more magic methods I want to talk about: ``__repr__`` and
``__str__``. The others are waiting for you to explore.

.. code-block:: python

    class Animal(object):

        def __init__(self, name, age):
            self.name = name
            self.age = age


    duck = Animal('Boo', 1)
    print(duck)

You will see:

.. code-block:: text

    <__main__.Animal object at 0x000001DF6DED8430>

We knows it's memory address but can hardly understand what it means.
``__repr__`` must be the way to help.

.. code-block:: python

    class Animal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<Animal: ' + self.name + '>'


    duck = Animal('Boo', 1)
    print(duck)

Then it's like:

.. code-block:: text

    <Animal: Boo>

``__repr__`` is a way to help us developers recognize each instance.

What about ``__str__``? Let's see:

.. code-block:: python

    class Animal(object):

        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __str__(self):
            return self.name


    duck = Animal('Boo', 1)
    print(duck)

Output:

.. code-block:: text

    Boo

It seems the same to ``__repr__``, just print what we want.

But actually, as a practical matter, ``__str__`` is always for the users,
``__repr__`` is for the developers. ``__str__`` is the way to print what it is,
while ``__repr__`` is used to distinguish instances during the development.
