class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        idx = 1
        nums.sort()

        for num in nums:
            if num == idx:
                idx += 1
        return idx
        