# -*- coding: utf-8 -*-

import pytest


def test_listiterator_len():
    with pytest.raises(TypeError):
        len(iter([1, 2, 3]))


def test_listiterator_length_hint():
    it = iter([1, 2, 3])
    assert it.__length_hint__() == 3
    it.next()
    assert it.__length_hint__() == 2
    it.next()
    assert it.__length_hint__() == 1
    it.next()
    assert it.__length_hint__() == 0
