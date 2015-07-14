# -*- coding: utf-8 -*-

import pytest


def test_pytest_raises():
    def f():
        raise ValueError('f')

    pytest.raises(ValueError, f)
    with pytest.raises(ValueError) as e:
        f()
    assert e.value.message == 'f'


def test_pytest_raises_regexp():
    def f():
        raise ValueError('f')

    pytest.raises_regexp(ValueError, 'f', f)
    with pytest.raises_regexp(ValueError, 'f') as e:
        f()
