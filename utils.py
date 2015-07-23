# -*- coding: utf-8 -*-

def filter_dict(f, d):
    return {k: v for k, v in d.iteritems() if f(k, v)}


def isiterator(it):
    return hasattr(it, '__iter__')


def hashable(object):
    return bool(getattr(object, '__hash__'))


def _assert(object, exc=AssertionError):
    if not object:
        raise exc
