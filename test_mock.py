# -*- coding: utf-8 -*-

import mock
import os

def test_mock_patch_object():
    with mock.patch.object(os, 'sys', mock.Mock(return_value=100)):
        assert os.sys() == 100

    with mock.patch.object(os, 'sys', return_value=101):
        assert os.sys() == 101
