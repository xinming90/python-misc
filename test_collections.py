# -*- coding: utf-8 -*-

import collections


def test_defaultdict_int():
    d = collections.defaultdict(int)
    assert dict(d) == {}
    d['name']
    assert dict(d) == {'name': 0}


def test_defaultdict_list():
    names = [
        'raymond', 'rachel', 'matthew', 'roger',
        'betty', 'melissa', 'judith', 'charlie',
    ]

    def f1(names):
        d = {}
        for name in names:
            key = len(name)
            if key not in d:
                d[key] = []
            d[key].append(name)
        return d

    def f2(names):
        d = {}
        d = collections.defaultdict(list)
        for name in names:
            d[len(name)].append(name)
        return d

    assert f1(names) == f2(names)


def test_OrderedDict():
    d = {}
    d[5] = 5
    d[0] = 0
    assert list(d.keys()) == [5, 0]

    od = collections.OrderedDict()
    od[5] = 5
    od[0] = 0
    assert list(od.keys()) == [5, 0]

    od[5] = 15
    assert list(od.keys()) == [5, 0]
