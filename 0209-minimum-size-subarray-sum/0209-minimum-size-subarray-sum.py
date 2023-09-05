class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        n = len(nums)
        cur_sum  = 0
        min_val = float("inf")

        for r in range(n):
            cur_sum += nums[r]
            while cur_sum >= target:
                min_val = min(min_val, r - l + 1)
                cur_sum -= nums[l]
                l += 1
                
        return min_val if min_val != float("inf") else 0