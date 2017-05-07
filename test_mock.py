# -*- coding: utf-8 -*-

import os

from unittest import mock


def test_mock_patch_object():
    with mock.patch.object(os, 'sys', mock.Mock(return_value=100)):
        assert os.sys() == 100

    with mock.patch.object(os, 'sys', return_value=101):
        assert os.sys() == 101


def test_mock_assert_has_calls():
    m = mock.Mock()
    m(1)
    m(2)
    m.assert_has_calls([mock.call(1), mock.call(2)])


def test_mock_call_args_list():
    m = mock.Mock()
    m(1)
    m(2)
    assert [mock.call(1), mock.call(2)] == m.call_args_list
