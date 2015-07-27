# -*- coding: utf-8 -*-

import pytest


def test_generator_len():
    with pytest.raises(TypeError):
        len(i for i in range(10))
