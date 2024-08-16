#!/usr/bin/env python3
""" Returns the key of the new data added"""
import redis
import uuid
from typing import Union


class Cache():
    """creating cache"""
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()
        
    def store(self, data:Union[int, float, bytes, str]):
        """Storing data in a cache"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
