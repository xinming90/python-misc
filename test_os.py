# -*- coding: utf-8 -*-

import os


def test_os_mkdir():
    # init
    os.mkdir('/tmp/dir')
    # os.chdir('/tmp/dir')
    # os.umask(2)

    # man 2 umask
    # man 2 mkdir
    # os.mkdir('tmp', 0775)
    # assert oct(os.stat('tmp').st_mode & 4095) == '0775'
    # assert oct(~2 & 777) == '0775'
    # os.rmdir('tmp')

    # os.umask(000)
    # os.mkdir('tmp', 777)
    # assert oct(os.stat('tmp').st_mode & 4095) == '0777'
    # assert oct(~000 & 775) == '0775'
    # os.rmdir('tmp')
    os.rmdir('/tmp/dir')
