# -*- coding: utf-8 -*-

import pytest

def test_dict_in():
    class D(dict):
        id = 10s

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

