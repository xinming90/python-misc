# -*- coding: utf-8 -*-

import datetime
import pytest
import mock

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


def test_setflag():
    m = mock.MagicMock(return_value=True)
    with pytest.raises(TypeError):
        setattr(datetime.datetime, 'now', m)
    _utils.setflag(datetime.datetime)
    setattr(datetime.datetime, 'now', m)
    assert datetime.datetime.now() is True


def test__assert():
    with pytest.raises(AssertionError):
        utils._assert(1 == 0)

    with pytest.raises(ValueError) as e:
        utils._assert(1 == 0, ValueError('py'))
    assert e.value.message == 'py'

    _utils._assert(1 == 1)
    with pytest.raises(AssertionError):
        _utils._assert(1 == 0)

    with pytest.raises(ValueError) as e:
        _utils._assert(1 == 0, ValueError('py'))
    assert e.value.message == 'py'


def test_ilen():
    assert _utils.ilen(iter([1, 2, 3])) == 3
    assert _utils.ilen(iter({'k': 'v', 'name': 'eleme'})) == 2
    assert _utils.ilen(iter((1, 2, 3))) == 3
    assert _utils.ilen(iter('eleme')) == 5


def test_glen():
    assert utils.glen(i for i in [3, 9, 2]) == 3
    assert _utils.glen(i for i in [3, 9, 2]) == 3


def test_call():
    def f():
        return True
    assert utils.call(f) is True
    assert _utils.call(f) is True
