# -*- coding: utf-8 -*-

import pytest

def test_class_eq():
    C = type('C', (object,), {})
    C == 1

    class MetaClass(type):
        def __eq__(cls, other):
            raise NotImplementedError

    class C(object):
        __metaclass__ = MetaClass

    with pytest.raises(NotImplementedError):
        C == 1
