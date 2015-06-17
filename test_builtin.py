# -*- coding: utf-8 -*-

import builtin

def test_filter():
    assert filter(None, [1, 0, 2]) == [1, 2]
    assert builtin.filter(None, [1, 0, 2]) == [1, 2]

    assert filter(bool, [1, 0, 2]) == [1, 2]
    assert builtin.filter(bool, [1, 0, 2]) == [1, 2]
