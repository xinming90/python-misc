# -*- coding: utf-8 -*-

import cPickle as pickle
import decimal

def test_pickle_decimal():
    d = {'name': 'eleme', 'k': decimal.Decimal(1)}
    r = pickle.loads(pickle.dumps(d))
    assert r == d
    assert isinstance(r['k'], decimal.Decimal)
