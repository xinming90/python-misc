# -*- coding: utf-8 -*-

import pytest


def test_class_eq():
    C = type('C', (object,), {}) # noqa
    C == 1

    class MetaClass(type):
        def __eq__(cls, other): # noqa
            raise NotImplementedError

    C = MetaClass('C', (object,), {}) # noqa
    with pytest.raises(NotImplementedError):
        C == 1
