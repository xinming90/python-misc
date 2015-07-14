# -*- coding: utf-8 -*-

import types
import _types

def test_function_type():
    def f():
        pass

    assert type(f) is types.FunctionType
    assert type(f) is _types.FunctionType


def test_lambda_type():
    f = lambda: None
    assert type(f) is types.LambdaType
    assert type(f) is _types.LambdaType


def test_code_type():
    def f():
        pass
    assert type(f.func_code) is types.CodeType
    assert type(f.func_code) is _types.CodeType


def test_generator_type():
    def g():
        yield
    assert type(g()) is types.GeneratorType
    assert type(g()) is _types.GeneratorType


def test_class_type():
    class C:
        pass
    assert type(C) is types.ClassType
    assert type(C) is _types.ClassType


def test_module_type():
    assert type(types) is types.ModuleType
    assert type(types) is _types.ModuleType


def test_type_type():
    assert type(type) is types.TypeType
    assert type(type) is _types.TypeType


def test_dict_proxy_type():
    assert type(type.__dict__) is types.DictProxyType
    assert type(type.__dict__) is _types.DictProxyType