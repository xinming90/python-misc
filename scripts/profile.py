# -*- coding: utf-8 -*-

import time
import datetime
import contextlib
import pstats
import cProfile
import StringIO


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
