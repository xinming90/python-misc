# -*- coding: utf-8 -*-

from utils import filter_dict

def test_filter_dict():
    d = {
        'name': 'eleme',
        '_name': 'e',
    }

    def f(k, v):
        return not k.startswith('_')

    assert filter_dict(f, d) == {'name': 'eleme'}

    f = lambda k, v: not k.startswith('_')
    assert filter_dict(f, d) == {'name': 'eleme'}
