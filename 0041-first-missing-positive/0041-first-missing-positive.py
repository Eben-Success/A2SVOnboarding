class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        num = 1

        nums.sort()

        for i in range(len(nums)):
            if nums[i] == num:
                num += 1
        return num

