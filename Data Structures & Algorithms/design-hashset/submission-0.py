class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
        
    def _hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        bucket_idx = self._hash(key)
        if key not in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].append(key)

    def remove(self, key: int) -> None:
        bucket_idx = self._hash(key)
        if key in self.buckets[bucket_idx]:
            self.buckets[bucket_idx].remove(key)

    def contains(self, key: int) -> bool:
        bucket_idx = self._hash(key)
        return key in self.buckets[bucket_idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
