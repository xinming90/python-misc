# -*- coding: utf-8 -*-

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
