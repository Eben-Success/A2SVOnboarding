class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # [0, 1, 3]
        # num = 0
        # nums.sort()
        # for i in range(len(nums)):
        #     if num == nums[i]:
        #         num += 1
        # return num

        hashset = set(nums)
        num = 0

        for num in range(len(nums) + 1):
            if num not in hashset:
                return num