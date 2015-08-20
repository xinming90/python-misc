# -*- coding: utf-8 -*-

import time
import datetime
import contextlib
import pstats
import cProfile
import StringIO


def unpatch_gevent_all():
    do_nothing = lambda *args, **kwds: None
    import gevent.monkey
    setattr(gevent.monkey, 'patch_all', do_nothing)
    setattr(gevent.monkey, 'patch_os', do_nothing)
    setattr(gevent.monkey, 'patch_time', do_nothing)
    setattr(gevent.monkey, 'patch_thread', do_nothing)
    setattr(gevent.monkey, 'patch_sys', do_nothing)
    setattr(gevent.monkey, 'patch_socket', do_nothing)
    setattr(gevent.monkey, 'patch_select', do_nothing)
    setattr(gevent.monkey, 'patch_ssl', do_nothing)
    setattr(gevent.monkey, 'patch_subprocess', do_nothing)

unpatch_gevent_all()


@contextlib.contextmanager
def profile(sort_by="cumulative"):
    p = cProfile.Profile()
    now = datetime.datetime.now()
    start = time.time()
    p.enable()
    yield
    p.disable()
    stop = time.time()
    s = StringIO.StringIO()
    pstats.Stats(p, stream=s).sort_stats(sort_by).print_stats()
    print s.getvalue()
    print "now = {}\n|{}ms".format(now, (stop - start) * 1000)


with profile("time"):
    pass
