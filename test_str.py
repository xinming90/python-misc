# -*- coding: utf-8 -*-

import pytest

def test_str_join():
    s = ' '
    assert s.join(['a', 'b']) == 'a b'

    with pytest.raises(TypeError):
        s.join('a', 'b')

    class String(str):
        def join(self, *args):
            if len(args) != 1:
                return str.join(self, args)
            return str.join(self, args[0])

    s = String(' ')
    assert s.join(['a', 'b']) == 'a b'
    assert s.join('a', 'b') == 'a b'


def test_str_split():
    assert 'xx.yyyy.zzz'.split('.') == ['xx', 'yyyy', 'zzz']
    assert 'xx.yyyy.zzz'.split('.', 0) == ['xx.yyyy.zzz']
    assert 'xx.yyyy.zzz'.split('.', 1) == ['xx', 'yyyy.zzz']
    assert 'xx.yyyy.zzz'.split('.', 2) == ['xx', 'yyyy', 'zzz']


def test_str_startswith():
    assert 'eleme'.startswith('ele') is True
    assert 'eleme'.startswith('eme') is False
    assert 'eleme'.startswith(('eme', 'ele')) is True


def test_str_endswith():
    assert 'eleme'.endswith('ele') is False
    assert 'eleme'.endswith('eme') is True
    assert 'eleme'.endswith(('eme', 'ele')) is True
