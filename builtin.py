# -*- coding: utf-8 -*-

import functools


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

        if hasattr(x, '__bool__'):
            return x.__bool__()

        if hasattr(x, '__len__'):
            return x.__len__()

        return True


class staticmethod(object):
    """
    staticmethod(function) -> method

    Convert a function to be a static method.

    A static method does not receive an implicit first argument.
    To declare a static method, use this idiom:

         class C:
         def f(arg1, arg2, ...): ...
         f = staticmethod(f)

    It can be called either on the class (e.g. C.f()) or on an instance
    (e.g. C().f()).  The instance is ignored except for its class.

    Static methods in Python are similar to those found in Java or C++.
    For a more advanced concept, see the classmethod builtin.
    """
    def __init__(self, function):
        self.function = function

    def __get__(self, obj, type=None):
        return self.function

""" implement in func
def staticmethod(function):
    class C(object):
        def __get__(self, obj, type=None):
            return function
    return C()
"""


class classmethod(object):
    """
    classmethod(function) -> method

    Convert a function to be a class method.

    A class method receives the class as implicit first argument,
    just like an instance method receives the instance.
    To declare a class method, use this idiom:

      class C:
          def f(cls, arg1, arg2, ...): ...
          f = classmethod(f)

    It can be called either on the class (e.g. C.f()) or on an instance
    (e.g. C().f()).  The instance is ignored except for its class.
    If a class method is called for a derived class, the derived class
    object is passed as the implied first argument.

    Class methods are different than C++ or Java static methods.
    If you want those, see the staticmethod builtin.
    """
    def __init__(self, function):
        self.function = function

    def __get__(self, obj, type=None):
        return functools.partial(self.function, type)


""" implement in func
def classmethod(function):
    class C(object):
        def __get__(self, obj, type=None):
            return functools.partial(function, type)
    return C()
"""


class property(object):
    """
    property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

    fget is a function to be used for getting an attribute value, and likewise
    fset is a function for setting, and fdel a function for del'ing, an
    attribute.  Typical use is to define a managed attribute x:

    class C(object):
        def getx(self): return self._x
        def setx(self, value): self._x = value
        def delx(self): del self._x
        x = property(getx, setx, delx, "I'm the 'x' property.")

    Decorators make defining new properties or modifying existing ones easy:

    class C(object):
        @property
        def x(self):
            "I am the 'x' property."
            return self._x
        @x.setter
        def x(self, value):
            self._x = value
        @x.deleter
        def x(self):
            del self._x
    """
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.doc = doc

    def setter(self, fset):
        """Descriptor to change the setter on a property."""
        self.fset = fset
        return self

    def deleter(self, fget):
        "Descriptor to change the deleter on a property."
        self.fdel = fget
        return self

    def __set__(self, obj, value):
        return self.fset(obj, value)

    def __get__(self, obj, type=None):
        return self.fget(obj)

    def __delete__(self, obj):
        return self.fdel(obj)


def callable(object):
    """
    callable(object) -> bool

    Return whether the object is callable (i.e., some kind of function).
    Note that classes are callable, as are instances with a __call__() method.
    """
    return hasattr(object, '__call__')
