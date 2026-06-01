class MyHashMap:

    def __init__(self):
        self.myHash = dict()

    def put(self, key: int, value: int) -> None:
        # if key not in self.myHash.keys():
        #     self.myHash[key] = value
        self.myHash[key] = value

    def get(self, key: int) -> int:
        if key not in self.myHash.keys():
            return -1
        return self.myHash.get(key)

    def remove(self, key: int) -> None:
        if key in self.myHash.keys():
            self.myHash.pop(key)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)