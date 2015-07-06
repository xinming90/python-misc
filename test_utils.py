# -*- coding: utf-8 -*-

import utils
import _utils

import pytest

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


def test_hashable():
    assert utils.hashable(1) is True
    assert utils.hashable('str') is True
    assert utils.hashable(u'unicode') is True
    assert utils.hashable([]) is False
    assert utils.hashable(set()) is False
    assert utils.hashable({}) is False

    assert _utils.hashable(1) is True
    assert _utils.hashable('str') is True
    assert _utils.hashable(u'unicode') is True
    assert _utils.hashable([]) is False
    assert _utils.hashable(set()) is False
    assert _utils.hashable({}) is False
