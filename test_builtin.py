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


def test_setattr():
    c = type('C', (object,), {})()
    assert hasattr(c, 'name') is False
    setattr(c, 'name', None)
    assert hasattr(c, 'name') is True

    c = type('C', (object,), {})()
    assert hasattr(c, 'name') is False
    builtin.setattr(c, 'name', None)
    assert hasattr(c, 'name') is True


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


def test_staticmethod():
    class C(object):
        @staticmethod
        def f():
            return 'f'

    assert C.f() == 'f'
    assert C().f() == 'f'

    class C(object):
        @builtin.staticmethod
        def f():
            return 'f'
    assert C.f() == 'f'
    assert C().f() == 'f'



def test_classmethod():
    class C(object):
        n = 10
        @classmethod
        def f(cls):
            return cls.n
    assert C.f() == 10
    assert C().f() == 10

    class C(object):
        n = 10
        @builtin.classmethod
        def f(cls):
            return cls.n
    assert C.f() == 10
    assert C().f() == 10


def test_property():
    class C(object):
        def getx(self):
            return 'x = {}'.format(self._x)

        def setx(self, value):
            self._x = value

        def delx(self):
            del self._x
        x = property(getx, setx, delx, "I'm the 'x' property.")

    c = C()
    c.x = 10
    assert c.x == 'x = 10'
    del c.x
    with pytest.raises(AttributeError):
        c.x


    class C(object):
        def getx(self):
            return 'x = {}'.format(self._x)

        def setx(self, value):
            self._x = value

        def delx(self):
            del self._x
        x = builtin.property(getx, setx, delx, "I'm the 'x' property.")

    c = C()
    c.x = 10
    assert c.x == 'x = 10'
    del c.x
    with pytest.raises(AttributeError):
        c.x


def test_property_decorator():
    class C(object):
        @property
        def x(self):
            return 'x = {}'.format(self._x)

        # import IPython; IPython.embed()
        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x

    c = C()
    c.x = 10
    assert c.x == 'x = 10'
    del c.x
    with pytest.raises(AttributeError):
        c.x


    class C(object):
        @builtin.property
        def x(self):
            return 'x = {}'.format(self._x)

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x

    c = C()
    c.x = 10
    assert c.x == 'x = 10'
    del c.x
    with pytest.raises(AttributeError):
        c.x


def test_callable():
    def f(): pass
    assert callable(len) is True
    assert callable("a") is False
    assert callable(callable) is True
    assert callable(lambda x, y: x + y) is True
    assert callable(__builtins__) is False
    assert callable(f) is True

    assert builtin.callable(len) is True
    assert builtin.callable("a") is False
    assert builtin.callable(callable) is True
    assert builtin.callable(lambda x, y: x + y) is True
    assert builtin.callable(__builtins__) is False
    assert builtin.callable(f) is True
