# -*- coding: utf-8 -*-

def filter_dict(f, d):
    return {k: v for k, v in d.iteritems() if f(k, v)}


def isiterator(it):
    return hasattr(it, '__iter__')
