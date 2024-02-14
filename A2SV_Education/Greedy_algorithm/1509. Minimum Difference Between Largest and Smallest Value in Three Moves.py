class Solution:
    def minDifference(self, nums: List[int]) -> int:

        if len(nums) <= 3:
            return 0

        nums.sort()

        nums1 = nums[:-3]
        diff1 = max(nums1) - min(nums1)

        nums2 = nums[3:]
        diff2 = max(nums2) - min(nums2)

        nums3 = nums[1:-2]
        diff3 = max(nums3) - min(nums3)

        nums4 = nums[2:-1]
        diff4 = max(nums4) - min(nums4)

        return min(diff4, diff3, diff2, diff1)
