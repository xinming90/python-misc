# -*- coding: utf-8 -*-

import pytest


CO_COROUTINE = 0x0080


def test_iscoroutinefunction():
    async def coro():
        pass

    assert coro.__code__.co_flags & CO_COROUTINE


def test_iter_coroutine():
    async def coro():
        pass

    c = coro()
    with pytest.raises(TypeError):
        iter(c)
