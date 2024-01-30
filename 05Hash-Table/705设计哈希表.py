class MyHashSet:

    def __init__(self):
        self.buckets = 10
        self.table = [[] for _ in range(self.buckets)]
    
    def hash(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        value = self.hash(key)
        if key not in self.table[value]:
            self.table[value].append(key)


    def remove(self, key: int) -> None:
        value = self.hash(key)
        if key in self.table[value]:
            self.table[value].remove(key)

    def contains(self, key: int) -> bool:
        value = self.hash(key)
        return key in self.table[value]



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)