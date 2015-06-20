# -*- coding: utf-8 -*-


def filter(function_or_none, sequence): # known special case of filter
    """
    filter(function or None, sequence) -> list, tuple, or string

    Return those items of sequence for which function(item) is true.  If
    function is None, return the items that are true.  If sequence is a tuple
    or string, return the same type, else return a list.
    """
    if function_or_none in (None, bool):
        return [item for item in sequence if item]
    return [item for item in sequence if function_or_none(item)]


def any(iterable):
    """
    any(iterable) -> bool
    
    Return True if bool(x) is True for any x in the iterable.
    If the iterable is empty, return False.
    """
    for item in iterable:
        if item:
            return True
    return False


def all(iterable):
    """
    all(iterable) -> bool

    Return True if bool(x) is True for all values x in the iterable.
    If the iterable is empty, return True.
    """
    for item in iterable:
        if not item:
            return False
    return True


def bool(x):
    """
    bool(x) -> bool

    Returns True when the argument x is true, False otherwise.
    The builtins True and False are the only two instances of the class bool.
    The class bool is a subclass of the class int, and cannot be subclassed.
    """
    if x is True:
        return True

    if x is False:
        return False

    if x is None:
        return False

    if hasattr(x, '__nonzero__'):
        return x.__nonzero__()

    if hasattr(x, '__len__'):
        return x.__len__()

    return True
