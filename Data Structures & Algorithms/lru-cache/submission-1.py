class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right

        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to most recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        # Key already exists
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = ListNode(key, value)
        self.cache[key] = node

        # Add as most recently used
        self.insert(node)

        # Remove least recently used
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]