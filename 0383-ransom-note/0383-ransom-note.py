class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # hash_1 = defaultdict(int)

        # for char in magazine:
        #     hash_1[char] += 1

        # for char in ransomNote:
        #     hash_1[char] -= 1

        # return all(num >= 0 for num in hash_1.values())


        rans = [0] * 26
        mag = [0] * 26

        for char in ransomNote:
            rans[ord(char) - ord('a')] += 1

        for char in magazine:
            mag[ord(char) - ord('a')] += 1


        for i in range(26):
            if mag[i] < rans[i]:
                return False
        return True

        

        


        


        