# -*- coding: utf-8 -*-

import pytest


CO_GENERATOR = 0x0020


def test_generator_len():
    with pytest.raises(TypeError):
        len(i for i in range(10))


def test_isgeneratorfunction():
    def gen():
        yield 1

    assert gen.__code__.co_flags & CO_GENERATOR


def test_generator_iterator():
    def gen():
        yield 1

    g = gen()
    it = iter(g)
    assert it is g
