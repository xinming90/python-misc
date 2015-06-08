# -*- coding: utf-8 -*-

class D(dict):
    id = 10


def test_dict_in():    
    d = D()
    d.id = 10
    assert 'id' not in d
    d['id'] = 11
    assert 'id' in d
