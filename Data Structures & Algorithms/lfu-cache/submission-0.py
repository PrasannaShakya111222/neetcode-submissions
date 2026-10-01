class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.next = self.right
        node.prev = self.right.prev

        self.right.prev.next = node
        self.right.prev = node

    def remove_last(self):
        if self.left.next == self.right:
            return None
        node = self.left.next
        self.remove(node)
        return node

    def is_empty(self):
        return self.left.next == self.right

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # key -> Node
        self.cache = {}
        # frequency -> Doubly Linked List
        self.freq = {}
        # Smallest frequency currently in cache
        self.min_freq = 0

    def _update(self, node):
        old_freq = node.freq
        # Remove node from old frequency list
        self.freq[old_freq].remove(node)
        # If this was last node with minimum frequency
        if old_freq == self.min_freq and self.freq[old_freq].is_empty():
            self.min_freq += 1
        # Increase frequency
        node.freq += 1
        # Create frequency list if necessary
        if node.freq not in self.freq:
            self.freq[node.freq] = DLL()
        # Add to most recently used position
        self.freq[node.freq].insert(node)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        # Using key increases its frequency
        self._update(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        # Key already exists
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            # Updating key counts as using it
            self._update(node)
            return
        # Cache is full
        if self.size == self.capacity:
            lfu_list = self.freq[self.min_freq]
            # Remove least recently used node
            node = lfu_list.remove_last()
            del self.cache[node.key]
            self.size -= 1
        # Add new node
        node = Node(key, value)
        self.cache[key] = node
        # New nodes always have frequency 1
        if 1 not in self.freq:
            self.freq[1] = DLL()
        self.freq[1].insert(node)
        self.min_freq = 1
        self.size += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)