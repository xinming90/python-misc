# -*- coding: utf-8 -*-


import contextlib
import pytest

def test_with_return():
    @contextlib.contextmanager
    def ctx():
        yield
        raise TypeError

    def f():
        with ctx():
            return 'x'

    with pytest.raises(TypeError):
        f()
