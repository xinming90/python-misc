# -*- coding: utf-8 -*-

import pytest


def test_pytest_raises():
    def f():
        raise ValueError('f')

    with pytest.raises(ValueError) as e:
        f()
    assert e.value.message == 'f'
