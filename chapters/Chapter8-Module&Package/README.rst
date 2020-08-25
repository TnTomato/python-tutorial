Module and Package
==================

Module
------

The module is like one or some files(.py) contains Python code. It helps you
orgnize your code blocks logically.

There are several built-in modules. Let's take ``sys`` as an example. Create
a file called `example.py`_ and put the following code inside:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import sys

    print(sys.argv[0])

``sys`` is one of Python's built-in modules, for doing some system stuff. Then
we run `example.py`_ in command line using Python command:

.. code-block:: text

    E:\project\python-tutorial\chapters\Chapter8-Module&Package>python example.py
    example.py

We see that ``print(sys.argv[0])`` leads to the result ``example.py``.
Telling you that ``sys.argv[0]`` always return the first argument of Python
command: the executing py-file.

So, like ``sys``, we can build modules on our own. Let's create a file named
`alpha.py`_:

.. code-block:: python

    # -*- coding: utf-8 -*-
    foo = 10
    bar = 'I am alpha'


    def do_print(obj):
        print(obj)


    class Animal(object):

        def __init__(self, name):
            self.name = name

        def call(self):
            print(self.name)


    if __name__ == '__main__':
        do_print(bar)


We declare some variables and define a function called ``do_print`` and a class.
See ``if __name__ == '__main__':``? It means the following code will be executed
when this py-file runs as a script.

Output:

.. code-block:: text

    I am alpha

Let's now create another file called `beta.py`_ and import some stuff from
`alpha.py`_:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import alpha

    biu = 'I am beta.py'

    print(alpha.foo)

    alpha.do_print(biu)

    dog = alpha.Animal('Jack')
    dog.call()


Run `beta.py`_, you will see:

.. code-block:: text

    Jack
    10
    I am beta.py

We use dot(.) to access stuffs from a module. You can see the code blocks in
``if __name__ == '__main__':`` never be executed when the file acts as a module
who is imported by others.

import
------

We use the keyword ``import`` to import modules. When ``import`` execute, the
python interpreter find the module from ``sys.path``:

>>> import sys
>>> sys.path
['', 'C:\\Users\\TnTomato\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\TnTomato\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\TnTomato\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\TnTomato\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\TnTomato\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']

It's a list of all search path. The first element is the script's directory or
''. Then we can easily edit ``sys.path`` to import modules from other places.

Like what in `beta.py`_, ``import`` should be at the head of a file with a
module name following. You can also give it an alias:

.. code-block:: python

    # -*- coding: utf-8 -*-
    import alpha as alp

    print(alp.foo)  # 10


There is another way of ``import``, try ``from ... import ...``:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from alpha import foo, Animal

    dog = Animal('Lisa')
    dog.call()  # Lisa
    print(foo)  # 10


Or ``from ... import *``:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from alpha import *

    print(foo)  # 10
    print(bar)  # I am alpha


You can use a asterisk(*) as all stuffs from the module, though it's not
recommended.

Package
-------

Package is a larger concept than module. Let's see the tree of the folder
**pkgexample**:

.. code-block:: text

    pkgexample/
        pkgalpha/
            __init__.py
            utils.py
        pkgbeta/
            __init__.py
            utils.py
        __init__.py

Python take a folder with a **__init__.py** as a package. Then we can import
something from the package, see `pkg.py`_:

.. code-block:: python

    # -*- coding: utf-8 -*-
    from pkgexample.pkgalpha.utils import alpha_intro
    from pkgexample.pkgbeta.utils import beta_intro

    alpha_intro()
    beta_intro()


.. _example.py: https://github.com/TnTomato/python-tutorial/tree/master/chapters/Chapter8-Module%26Package/example.py
.. _alpha.py: https://github.com/TnTomato/python-tutorial/tree/master/chapters/Chapter8-Module%26Package/alpha.py
.. _beta.py: https://github.com/TnTomato/python-tutorial/tree/master/chapters/Chapter8-Module%26Package/beta.py
.. _pkg.py: https://github.com/TnTomato/python-tutorial/tree/master/chapters/Chapter8-Module%26Package/pkg.py
