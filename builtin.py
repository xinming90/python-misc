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


def hasattr(object, name):
    """
    hasattr(object, name) -> bool

    Return whether the object has an attribute with the given name.
    (This is done by calling getattr(object, name) and catching exceptions.)
    """
    try:
        object.__getattribute__(name)
        return True
    except AttributeError:
        return False


def getattr(object, name, *default):
    """
    getattr(object, name[, default]) -> value

    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.
    """
    try:
        return object.__getattribute__(name)
    except AttributeError:
        if len(default) == 1:
            return default[0]
        raise


def setattr(object, name, value):
    """
    setattr(object, name, value)
    
    Set a named attribute on an object; setattr(x, 'y', v) is equivalent to
    ``x.y = v''.
    """
    object.__setattr__(name, value)


class bool(int):
    """
    bool(x) -> bool

    Returns True when the argument x is true, False otherwise.
    The builtins True and False are the only two instances of the class bool.
    The class bool is a subclass of the class int, and cannot be subclassed.
    """
    def __new__(cls, x):
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
