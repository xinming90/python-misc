# -*- coding: utf-8 -*-


def test_try_except_tuple():
    try:
        raise TypeError('')
    except (TypeError, ValueError):
        pass

    try:
        raise ValueError('')
    except (TypeError, ValueError):
        pass
