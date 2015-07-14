# -*- coding: utf-8 -*-

import unittest
import inspect


class MyTest(unittest.TestCase):
    def runTest(self):
        for name, method in inspect.getmembers(self, inspect.ismethod):
            if name.startswith('test_'):
                method()


def test_unittest_raises():
    def f():
        raise ValueError('f')

    class Test(MyTest):
        def test_raises(self):
            self.assertRaises(ValueError, f)

        def test_with_raises(self):
            with self.assertRaises(ValueError):
                f()

    t = Test()
    t.runTest()


def test_unittest_raises_regex():
    def f():
        raise ValueError('f')

    class Test(MyTest):
        def test_raises(self):
            self.assertRaisesRegexp(ValueError, 'f', f)

        def test_with_raises(self):
            with self.assertRaisesRegexp(ValueError, 'f'):
                f()

    t = Test()
    t.runTest()
