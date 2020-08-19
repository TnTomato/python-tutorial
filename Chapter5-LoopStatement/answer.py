# -*- coding: utf-8 -*-
"""
    Build a program to print a graph like:
           *
          ***
         *****
        *******
    Try to code as easy as you can.
"""
for i in range(1, 5):
    print(' ' * (4 - (i - 1)) + '*' * (2 * i - 1))
