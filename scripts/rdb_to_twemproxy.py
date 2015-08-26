# -*- coding: utf-8 -*-

import datetime
import redis

from rdbtools import RdbParser, RdbCallback
now = datetime.datetime.now


class MyCallback(RdbCallback):
    def __init__(self, r):
        self.redis = r
        self.count = 0
        self.p = r.pipeline(transaction=False)

    def set(self, key, value, expiry, info):
        print "set|{}|{}".format(key, value)
        self.p.set(key, value)
        self.execute()

    def hset(self, key, field, value):
        print "hset|{}|{}|{}".format(key, field, value)
        self.p.hset(key, field, value)
        self.execute()

    def sadd(self, key, member):
        print "sadd|{}|{}".format(key, member)
        self.redis.sadd(key, member)
        self.execute()

    def rpush(self, key, value) :
        print "rpush|{}|{}".format(key, value)
        self.redis.rpush(key, value)
        self.execute()

    def zadd(self, key, score, member):
        print "zadd|{}|{}|{}".format(key, member, score)
        self.redis.zadd(key, member, score)
        self.execute()

    def end_rdb(self):
        self.p.execute()

    def execute(self):
        self.count = (self.count + 1) % 10000
        if not self.count:
            self.p.execute()


r = redis.Redis.from_url("redis://127.0.0.1:6400")
callback = MyCallback(r)
parser = RdbParser(callback, filters={"dbs": [0]})
print "start {}".format(now())
parser.parse("/home/xinming.pan/dump.rdb")
print "stop {}".format(now())
