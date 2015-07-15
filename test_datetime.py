# -*- coding: utf-8 -*-

from datetime import (
    datetime,
    timedelta,
)


def test_timedelta():
    today = datetime(2015, 7, 15)
    delta = timedelta(days=1)
    assert today - delta == datetime(2015, 7, 14)
    assert today + delta == datetime(2015, 7, 16)

    delta = timedelta(days=-1)
    assert today - delta == datetime(2015, 7, 16)
    assert today + delta == datetime(2015, 7, 14)
