# -*- coding: utf-8 -*-

from io import StringIO
from functools import partial

import pytest


def test_unpack_iter():
    a, b = iter([9, 4])
    assert (a, b) == (9, 4)
    with pytest.raises(ValueError):
        a, = iter([9, 4])
    with pytest.raises(ValueError):
        a, b, c = iter([9, 4])

    def g():
        yield 19
        yield 14
    a, b = g()
    assert (a, b) == (19, 14)


def test_iter_sentinel():
    """Call a function until a sentinel value"""
    def w(s, n):
        s = StringIO(s)
        blocks = []
        while True:
            block = s.read(n)
            if block == '':
                break
            blocks.append(block)
        return blocks

    def f(s, n):
        s = StringIO(s)
        blocks = []
        for block in iter(partial(s.read, n), ''):
            blocks.append(block)
        return blocks

    assert w('abcde', 2) == ['ab', 'cd', 'e']
    assert f('abcde', 2) == ['ab', 'cd', 'e']
