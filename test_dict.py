# -*- coding: utf-8 -*-

def test_dict_in():    
    class D(dict):
        id = 10
    
    d = D()
    d.id = 10
    assert 'id' not in d
    d['id'] = 11
    assert 'id' in d


def test_dict_values():
    class D(dict):
        def values(self):
            return False

    d = D()
    d['name'] = 'eleme'
    assert d.values() is False
    assert dict.values(d) == ['eleme']
