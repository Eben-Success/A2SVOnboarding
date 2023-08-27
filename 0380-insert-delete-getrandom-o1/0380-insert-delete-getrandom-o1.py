class RandomizedSet:

    def __init__(self):
        self.hashmap = {}
        self.nums = []
        

    def insert(self, val: int) -> bool:
        if val not in self.hashmap:
            self.nums.append(val)
            self.hashmap[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            idx = self.hashmap[val]
            l_idx_elem = self.nums[-1]
            self.hashmap[l_idx_elem] = idx

            self.nums[idx], self.nums[len(self.nums)-1] = self.nums[len(self.nums) - 1], self.nums[idx]
            self.nums.pop()
            del self.hashmap[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()