# -*- coding: utf-8 -*-

import operator
import Operator


def test_iadd():
    class C(object):
        def __add__(self, other):
            return '__add__'

        def __iadd__(self, other):
            return '__iadd__'

    c = C()
    # c + 5
    assert operator.add(c, 5) == "__add__"
    assert Operator.add(c, 5) == '__add__'
    # c += 5
    assert operator.iadd(c, 5) == "__iadd__"
    assert Operator.iadd(c, 5) == '__iadd__'

    class C(object):
        def __add__(self, other):
            return '__add__'
    c = C()
    assert operator.iadd(c, 5) == "__add__"
    assert Operator.iadd(c, 5) == '__add__'


def test_list_add_iadd_diff():
    l2 = l1 = l = [1, 2]
    l1 = l1 + [3, 4]
    assert id(l) != id(l1)
    l2 += [3, 4]
    assert id(l) == id(l2)
