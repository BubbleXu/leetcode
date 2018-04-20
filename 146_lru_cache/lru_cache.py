# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following
# operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a new item.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
import collections


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = collections.OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.dict.get(key):
            value = self.dict.pop(key)
            self.dict[key] = value
            return self.dict[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.dict.get(key):
            self.dict.pop(key)
            self.dict[key] = value
            return

        if len(self.dict) < self.capacity:
            self.dict[key] = value
        else:
            self.dict.pop(self.dict.keys()[0])
            self.dict[key] = value


        # Your LRUCache object will be instantiated and called as such:
        # obj = LRUCache(capacity)
        # param_1 = obj.get(key)
        # obj.put(key,value)

if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(2, 1)
    cache.put(2, 2)
    print cache.get(2)
    cache.put(1, 1)
    cache.put(4, 1)
    print cache.get(2)
