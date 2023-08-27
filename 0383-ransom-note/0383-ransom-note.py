class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        hash_1 = defaultdict(int)

        for char in magazine:
            hash_1[char] += 1

        for char in ransomNote:
            hash_1[char] -= 1

        return all(num >= 0 for num in hash_1.values())

        

        


        


        