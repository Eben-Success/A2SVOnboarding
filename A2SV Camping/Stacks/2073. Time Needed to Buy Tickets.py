class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        queue = deque()
        count = 0
        
        for idx, num in enumerate(tickets): # O(n) time
            queue.append((num, idx))

        while queue:
            num, idx = queue.popleft()
            if num > 0: count += 1
            num -= 1
            if num == 0 and idx == k:
                break
            if num >= 0:
                queue.append((num, idx))

        return count

        
            

                
