class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        if k <= 1:
            return 0

        cur_product = 1
        l = 0
        count = 0
        n = len(nums)
        for r in range(n):
            cur_product *= nums[r]

            while cur_product >= k:
                cur_product /= nums[l]
                l += 1
            count += (r - l + 1)
        return count

        