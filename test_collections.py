# -*- coding: utf-8 -*-

import collections


def test_collections_defaultdict():
    d = collections.defaultdict(int)
    assert dict(d) == {}
    d['name']
    assert dict(d) == {'name': 0}
