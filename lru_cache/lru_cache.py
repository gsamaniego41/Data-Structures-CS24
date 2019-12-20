from doubly_linked_list import DoublyLinkedList

'''
LRU Cache 
Least recently used = tail
Most recently used = head
When we access an item, it moves up and becomes the new head.

    [0] [1] [2] [3]

    [2] [0] [1] [3]

When cache hits max capacity, 
    evict the LEAST recently used item (tail)

    [0] [1] [2] [3]    [4]
'''


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=3):
        self.limit = limit
        self.size = 0
        self.dll = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if key in self.storage:
            value = self.storage[key]
            self.dll.move_to_front(value)
            return value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # if key exists re-assign new value
        if key in self.storage:
            self.storage[key] = value
            # print(self.storage)
            self.dll.move_to_front({key: value})
            # self.dll.move_to_front({key: value})
            return f'Updated {self.storage[key]}, moved to head'
        # if max capacity
            # remove tail
            # add to head

        if self.size >= self.limit:
            # print('Max capacity')
            # del self.storage[self.dll.tail]
            self.dll.remove_from_tail()
            # self.size -= 1
            return 'Max capacity'

        self.dll.add_to_head({key: value})
        self.storage[key] = value
        self.size += 1


test = LRUCache()
# print(f'result: {test.set('name', 'GABRIEL')}')
# print(test.set('name', 'GABRIEL'))
print(test.set('QB', 'Josh Allen'))
print(test.storage)
print('\n-------------------\n')
print(test.set('WR1', 'Davante Adams'))
print(test.storage)
print('\n-------------------\n')
print(test.set('RB1', 'Aaron Jones'))
print(test.storage)
print('\n-------------------\n')
print(test.set('WR1', 'Tyreek Hill'))
print(test.storage)
print('\n-------------------\n')
print(f'head: {test.dll.head}')
print(f'tail: {test.dll.tail.value}')
print('\n-------------------\n')
print(test.set('DST', 'Steelers'))
print(test.storage)
# "name": "gabe", "role": "ux engineer"
