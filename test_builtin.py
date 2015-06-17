# -*- coding: utf-8 -*-

import builtin

def test_filter():
    assert filter(None, [1, 0, 2]) == [1, 2]
    assert builtin.filter(None, [1, 0, 2]) == [1, 2]

    assert filter(bool, [1, 0, 2]) == [1, 2]
    assert builtin.filter(bool, [1, 0, 2]) == [1, 2]


def test_any():
    assert any([1, 0, 2]) == True
    assert builtin.any([1, 0, 2]) == True


def test_all():
    assert all([1, 0, 2]) == False
    assert builtin.all([1, 0, 2]) == False
    assert all([]) == True
    assert builtin.all([]) == True
