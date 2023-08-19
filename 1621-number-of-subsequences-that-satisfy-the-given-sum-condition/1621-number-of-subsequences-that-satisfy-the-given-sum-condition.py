class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        mod = 10**9 + 7
        count = 0

        nums.sort()

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1

            else:
                count += pow(2, right - left)
                left += 1

        return count % mod