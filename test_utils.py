# -*- coding: utf-8 -*-

import utils
import _utils

def test_filter_dict():
    d = {
        'name': 'eleme',
        '_name': 'e',
    }

    def f(k, v):
        return not k.startswith('_')

    assert utils.filter_dict(f, d) == {'name': 'eleme'}

    f = lambda k, v: not k.startswith('_')
    assert utils.filter_dict(f, d) == {'name': 'eleme'}


def test_isiterator():
    assert utils.isiterator([]) is True
    assert utils.isiterator({}) is True
    assert utils.isiterator(None) is False

    assert _utils.isiterator([]) is True
    assert _utils.isiterator({}) is True
    assert _utils.isiterator(None) is False
