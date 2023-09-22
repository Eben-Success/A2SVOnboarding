class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # minimization problem: high
        
        n = len(letters)
        low, high = -1, n
        
        while (low + 1) < high:
            mid = ((high - low)//2) + low
            
            if letters[mid] > target:
                high = mid
            else:
                low = mid
                
        return letters[0] if high == n else letters[high]
        