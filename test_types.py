# -*- coding: utf-8 -*-

import types
import _types


def test_function_type():
    def f():
        pass

    assert type(f) is types.FunctionType # noqa
    assert type(f) is _types.FunctionType


def test_lambda_type():
    f = lambda: None # noqa
    assert type(f) is types.LambdaType # noqa
    assert type(f) is _types.LambdaType


def test_code_type():
    def f():
        pass
    assert type(f.__code__) is types.CodeType # noqa
    assert type(f.__code__) is _types.CodeType


def test_generator_type():
    def g():
        yield
    assert type(g()) is types.GeneratorType # noqa
    assert type(g()) is _types.GeneratorType


def test_module_type():
    assert type(types) is types.ModuleType # noqa
    assert type(types) is _types.ModuleType
