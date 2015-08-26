# -*- coding: utf-8 -*-

import datetime
import redis

from rdbtools import RdbParser, RdbCallback
now = datetime.datetime.now


class MyCallback(RdbCallback):
    def __init__(self, r):
        self.redis = r

    def set(self, key, value, expiry, info):
        print "set|{}|{}".format(key, value)
        # self.redis.set(key, value, expiry)
        self.redis.set(key, value)

    def hset(self, key, field, value):
        print "hset|{}|{}|{}".format(key, field, value)
        self.redis.hset(key, field, value)

    def sadd(self, key, member):
        print "sadd|{}|{}".format(key, member)
        self.redis.sadd(key, member)

    def rpush(self, key, value) :
        print "rpush|{}|{}".format(key, value)
        self.redis.rpush(key, value)

    def zadd(self, key, score, member):
        print "zadd|{}|{}|{}".format(key, member, score)
        self.redis.zadd(key, member, score)


r = redis.Redis.from_url("redis://127.0.0.1:6400")
callback = MyCallback(r)
parser = RdbParser(callback)
print "start {}".format(now())
parser.parse('/home/xinming.pan/dump.rdb')
print "stop {}".format(now())
