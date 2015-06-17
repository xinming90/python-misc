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
