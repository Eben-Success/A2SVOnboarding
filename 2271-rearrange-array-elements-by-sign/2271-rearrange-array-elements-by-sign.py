class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        pos = [num for num in nums if num > 0]
        neg = [num for num in nums if num < 0]

        res = []

        for p, n in zip(pos, neg):
            res += [p, n]

        return res
        
        