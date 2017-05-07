# -*- coding: utf-8 -*-

import Bool


def test_Bool():
    assert Bool.Bool(0) is Bool.false
    assert Bool.Bool(1) is Bool.true
    assert Bool.Bool(None) is Bool.false

    C = type('C', (object,), {})

    assert Bool.Bool(C()) is Bool.true

    C = type('C', (object,), {'__bool__': lambda self: False})
    assert Bool.Bool(C()) is Bool.false

    C = type('C', (object,), {'__len__': lambda self: False})
    assert Bool.Bool(C()) is Bool.false

    C = type('C', (object,), {'__bool__': lambda self: False,
                              '__len__': lambda self: True})
    assert Bool.Bool(C()) is Bool.false

    assert str(Bool.Bool(0)) == 'false'
    assert str(Bool.Bool(1)) == 'true'
    assert repr(Bool.Bool(0)) == 'false'
    assert repr(Bool.Bool(1)) == 'true'
