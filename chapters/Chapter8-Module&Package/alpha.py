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
