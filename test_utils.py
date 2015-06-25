# -*- coding: utf-8 -*-

from utils import filter_dict

def test_filter_dict():
    d = {
        'name': 'eleme',
        '_name': 'e',
    }

    def f(k, v):
        if k.startswith('_'):
            return False
        return True

    assert filter_dict(f, d) == {'name': 'eleme'}
