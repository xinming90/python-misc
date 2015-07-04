# -*- coding: utf-8 -*-

import types
import _types

def test_function():
    def f():
        pass

    assert type(f) is types.FunctionType
    assert type(f) is _types.FunctionType
