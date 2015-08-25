# -*- coding: utf-8 -*-

import collections


def test_collections_defaultdict():
    d = collections.defaultdict(int)
    assert dict(d) == {}
    d['name']
    assert dict(d) == {'name': 0}


def test_OrderedDict():
    d = {}
    d[5] = 5
    d[0] = 0
    assert d.keys() == [0, 5]

    od = collections.OrderedDict()
    od[5] = 5
    od[0] = 0
    assert od.keys() == [5, 0]

    od[5] = 15
    assert od.keys() == [5, 0]
