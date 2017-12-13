# -*- coding: utf-8 -*-


CO_COROUTINE = 0x0080


def test_iscoroutinefunction():
    async def coro():
        pass

    assert coro.__code__.co_flags & CO_COROUTINE