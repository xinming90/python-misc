# -*- coding: utf-8 -*-


def add(a, b):
    """ add(a, b) -- Same as a + b. """
    if hasattr(a, '__add__'):
        return a.__add__(b)


def iadd(a, b):
    """ a = iadd(a, b) -- Same as a += b. """
    if hasattr(a, '__iadd__'):
        return a.__iadd__(b)
    if hasattr(a, '__add__'):
        return a.__add__(b)
