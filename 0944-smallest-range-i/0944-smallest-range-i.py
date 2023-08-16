class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        # Time: O(n) | Space: O(1)

        max_val, min_val = max(nums), min(nums)
        min_score = max_val - min_val

        for num in nums:
            new_max = max_val - k
            new_min = min_val + k

            new_score = max(new_max - new_min, 0)

            min_score = min(min_score, new_score)

        return min_score