Class
=====

After you have learned how to define a function, you may think you've probably
got all the programming skills. Definitely not! Have you ever heard of
*Object Oriented Programming(OOP)*?

We've already used a word *object* several times in the previous chapters. Do
you really know what an object is? Follow me and I will tell the answer.

Definition
----------

The key of *Object Oriented Programming* is *class*. An object is an
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

        def make_a_sound(self):
            print(self.sound)


    duck = Animal('Boo', 1, 'quack')
    fish = Animal('Booboo', 2, 'mute')

    duck.make_a_sound()  # quack
    fish.make_a_sound()  # mute

Just use a dot(.) to call the method with the object.

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

Inheritance
-----------

Inheritance is one of the *Object Oriented Programming*'s features. A subclass
can possess its superclass's attributes, methods or customize them. We have
already defined a class called ``Animal``, Let's start from an example based
on this:

.. code-block:: python

    class Animal(object):

        def __init__(self, name, age, sound):
            self.name = name
            self.age = age
            self.sound = sound

        def make_a_sound(self):
            print(self.sound)


    class Dog(Animal):
        pass


    teddy = Dog('Lisa', 2, 'woof')
    print(teddy.name)  # Lisa
    print(teddy.age)  # 2
    teddy.make_a_sound()  # woof

You see clearly that the subclass ``Dog`` is inherited from ``Animal``.
Nothing is in class ``Dog`` but its instance can have all ``Animal``'s
attributes and methods.

Continue from the example above, we can customize some other attributes or
methods:

.. code-block:: python

    class Cat(Animal):

        def __init__(self, name, age, sound, food):
            super(Cat, self).__init__(name, age, sound)
            self.food = food

        def eat(self):
            print('I eat ' + self.food)


    garfield = Cat('Sherry', 2, 'meow', 'cat food')
    print(garfield.name)  # Sherry
    print(garfield.food)  # cat food
    garfield.eat()  # I eat cat food

We add a new attribute called ``food``. See
``super(Cat, self).__init__(name, age, sound)``? That is used to call the
superclass's method. We have added a new attribute ``food`` but still need
the other 3 attributes. So we have to call superclass's ``__init__``.

A new method called ``eat`` is also added to the new class ``Cat``. It's for
``Cat``'s instances only. There will be an exception when ``Dog``'s instance
call ``eat``:

.. code-block:: python

    teddy.eat()  # AttributeError: 'Dog' object has no attribute 'eat'

You can also rewrite method ``make_a_sound``:

.. code-block:: python

    class Fish(Animal):

        def __init__(self, name, age, sound):
            self.name = name
            self.age = age

        def make_a_sound(self):
            if self.sound:
                print(self.sound)
            else:
                print('I cannot make a sound')


    shark = Fish('Tom', 1, '')
    shark.make_a_sound()  # I cannot make a sound

As we can see, ``Fish`` has the same method as ``Animal``. But they can have
different implementations. This is called *override*.
