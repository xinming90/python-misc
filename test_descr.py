# -*- coding: utf-8 -*-

import pytest

def test_test():
    class C(object):
        def f(self):
            return 'I am f'
    with pytest.raises(TypeError):
        C.f()
    assert C().f() == 'I am f'

    class F(object):
        def __get__(self, obj, type=None):
            if obj is None:
                raise TypeError('unbound method f() must be '
                                'called with C instance as '
                                'first argument (got nothing instead)')
            return lambda: 'C.f'

    class C(object):
        f = F()

    with pytest.raises(TypeError):
        C.f()
    assert C().f() == 'C.f'
