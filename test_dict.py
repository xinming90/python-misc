# -*- coding: utf-8 -*-

import pytest

def test_dict_in():
    class D(dict):
        id = 10

    d = D()
    d.id = 10
    assert 'id' not in d
    d['id'] = 11
    assert 'id' in d


def test_dict_values():
    class D(dict):
        def values(self):
            return False

    d = D()
    d['name'] = 'eleme'
    assert d.values() is False
    assert dict.values(d) == ['eleme']


def test_dict_clear():
    class D(dict):
        def clear(self):
            pass

    d = D()
    d['name'] = 'eleme'
    assert 'name' in d

    d.clear()
    assert 'name' in d

    dict.clear(d)
    with pytest.raises(AssertionError):
        assert 'name' in d


def test_dict_update():
    class D(dict):
        def update(self, **kwds):
            pass

    d = D()
    assert d.keys() == []

    d.update(name='eleme')
    assert d.keys() == []

    dict.update(d, name='eleme')
    assert d.items()[0] == ('name', 'eleme')


def test_dict_dict():
    class D(dict):
        pass

    d = D()
    d['name'] = 'eleme'
    d.name = 'eme'
    assert dict(d) == {'name': 'eleme'}


def test_dict_get():
    class D(dict):
        def get(self, key):
            return None

    d = D()
    d['name'] = 'eleme'
    assert d.get('name') is None
    assert dict.get(d, 'name') == 'eleme'


def test_dict_getitem():
    d = {}
    d['k'] = {}.get('k')
    assert d == {'k': None}

    class D(dict):
        def __setitem__(self, key, value):
            if value:
                dict.__setitem__(self, key, value)

    d = D()
    d['k'] = {}.get('k')
    assert d == {}


def test_dict_iterator_length_hint():
    it = iter({'k': 'v', 'name': 'eleme'})
    assert it.__length_hint__() == 2
    it.next()
    assert it.__length_hint__() == 1
    it.next()
    assert it.__length_hint__() == 0


def test_dict_generator():
    d = {'k': 'v', 'name': 'eleme'}
    assert dict((k, v) for k, v in d.iteritems()) == d
