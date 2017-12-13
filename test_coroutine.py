# -*- coding: utf-8 -*-

import inspect
import pytest


CO_COROUTINE = 0x0080
CO_ITERABLE_COROUTINE = 0x0100


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


def test_next_coroutine():
    async def coro():
        pass

    c = coro()
    with pytest.raises(TypeError):
        next(c)


def test_coroutine_send():
    async def coro():
        return 'coro'

    c = coro()
    try:
        c.send(None)
    except StopIteration as e:
        assert e.value == 'coro'


def test_coroutine_awaitable():
    async def coro():
        pass

    assert inspect.isawaitable(coro())
