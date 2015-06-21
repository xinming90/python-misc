# -*- coding: utf-8 -*-

false = None
true = None

class Bool(int):
    def __new__(cls, x):
        global true, false
        if true is None:
            true = int.__new__(cls, 1)

        if false is None:
            false = int.__new__(cls, 0)

        if x is true:
            return true

        if x is false:
            return false

        if x is None:
            return false

        if hasattr(x, '__nonzero__'):
            if x.__nonzero__() is True:
                return true
            return false

        if hasattr(x, '__len__'):
            if x.__len__() is True:
                return true
            return false

        return true


    def __str__(self):
        if self.real == 1:
            return 'true'
        return 'false'

    __repr__ = __str__
