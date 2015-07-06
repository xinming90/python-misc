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
