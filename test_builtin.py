# -*- coding: utf-8 -*-

import pytest
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
    c = C()
    assert bool(c) is False
    assert builtin.bool(c) is False


def test_hasattr():
    C = type('C', (object,), {'name': 'C'})
    c = C()
    assert hasattr(c, 'name') is True
    assert hasattr(c, 'tname') is False
    assert builtin.hasattr(c, 'name') is True
    assert builtin.hasattr(c, 'tname') is False


def test_getattr():
    C = type('C', (object,), {'name': 'C'})
    c = C()
    assert getattr(c, 'name') == 'C'
    with pytest.raises(AttributeError):
        getattr(c, 'tname')
    assert getattr(c, 'tname', 'default') == 'default'

    assert builtin.getattr(c, 'name') == 'C'
    with pytest.raises(AttributeError):
        builtin.getattr(c, 'tname')
    assert builtin.getattr(c, 'tname', 'default') == 'default'


def test_getitem():
    class C(object):
        def __getitem__(self, i):
            start = i.start
            stop = i.stop
            if start in (None, 0):
                return 'LIMIT {}'.format(stop)
            return 'LIMIT {}, {}'.format(start, stop - start)

    c = C()
    assert c[:3] == 'LIMIT 3'
    assert c[0:3] == 'LIMIT 3'
    assert c[1:3] == 'LIMIT 1, 2'
