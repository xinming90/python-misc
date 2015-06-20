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


def test_bool():
    assert bool(True) is True
    assert builtin.bool(True) is True
    
    assert bool(False) is False
    assert builtin.bool(False) is False
    
    assert bool(None) is False
    assert builtin.bool(None) is False

    C = type('C', (object,), {})
    c = C()
    assert bool(c) is True
    assert builtin.bool(c) is True
    
    C = type('C', (object,), {'__nonzero__': lambda self: False})
    c = C()
    assert bool(c) is False
    assert builtin.bool(c) is False

    C = type('C', (object,), {'__len__': lambda self: False})
    c = C()
    assert bool(c) is False
    assert builtin.bool(c) is False
    
    # nonzero win
    C = type('C', (object,), {'__nonzero__': lambda self: False,
                              '__len__': lambda self: True})
    assert bool(C()) is False
    assert builtin.bool(C()) is False
