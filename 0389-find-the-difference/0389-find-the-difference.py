class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        if not s:
            return t

        hashmap = defaultdict(int)
        
        for char in s:
            hashmap[char] += 1
            
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
                if hashmap[char] == 0:
                    del hashmap[char]
            else:
                return char

        
        