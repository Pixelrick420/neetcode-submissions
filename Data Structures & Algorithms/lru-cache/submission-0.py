class Node:
    def __init__(self, key :int, value:int):
        self.key = key
        self.val = value
        self.nxt = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = LinkedList()
        self.n = 0
        self.capacity = capacity
        self.pointers = {}
    
    def remove(self, node):
        if not node:
            return

        prev = node.prev
        nxt = node.nxt

        if nxt:
            nxt.prev = prev
        
        else:
            self.cache.tail = prev
        
        if prev:
            prev.nxt = nxt
        
        else:
            self.cache.head = nxt
        
        node.nxt = node.prev = None
    
    def add(self, node):
        node.nxt = self.cache.head
        node.prev = None

        if self.cache.head:
            self.cache.head.prev = node
        else:
            self.cache.tail = node

        self.cache.head = node


    def get(self, key: int) -> int:
        if key in self.pointers:
            node = self.pointers[key]
            self.remove(node)
            self.add(node)

            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.pointers:
            node = self.pointers[key]
            node.val = value

            self.remove(node)
            self.add(node)
        
        elif self.n < self.capacity:
            self.n += 1

            node = Node(key, value)
            self.pointers[key] = node
            self.add(node)
        
        else:
            replace = self.cache.tail
            self.remove(replace)
            
            del self.pointers[replace.key]
            
            node = Node(key, value)
            self.pointers[key] = node
            self.add(node)
            self.cache.head = node

