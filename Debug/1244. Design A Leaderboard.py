import heapq

class LeaderShipBoard:
    
    def __init__(self):
        self.hasmap = {}

    def add_score(self, playerId: int, score: int) -> None:
        if playerId not in self.hashmap:
            self.hashmap[playerId] = score
        else:
            self.hashmap[playerId] += score
    
    def top(self, k: int) -> int:
        nums = list(self.hashmap.values())
        nums = [-num for num in nums]
        heapq.heapify(nums)
        total = 0
        
        while k > 0:
            total += - heapq.heappop(nums)
            k -= 1
        return total
        
    
    def reset(self, playerId: int) -> None:
        self.hashmap[playerId] = 0