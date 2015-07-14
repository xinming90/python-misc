# -*- coding: utf-8 -*-

import unittest
import inspect

def test_unittest_raise():
    def f():
        raise ValueError('f')

    class MyTest(unittest.TestCase):
        def test_raises(self):
            self.assertRaises(ValueError, f)

        def test_with_raises(self):
            with self.assertRaises(ValueError):
                f()

        def runTest(self):
            for name, method in inspect.getmembers(self, inspect.ismethod):
                if name.startswith('test_'):
                    method()

    t = MyTest()
    t.runTest()
