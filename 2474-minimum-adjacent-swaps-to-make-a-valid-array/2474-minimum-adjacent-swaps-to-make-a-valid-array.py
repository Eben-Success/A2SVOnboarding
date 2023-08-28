class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        min_idx = -1
        max_idx = len(nums)

        max_elem = max(nums)
        min_elem = min(nums)
        n = len(nums)

        for i in range(n):
            if nums[i] == max_elem:
                max_idx = i

            if nums[i] == min_elem:
                if min_idx == -1:
                    min_idx = i


        if min_idx > max_idx:
            return (n - max_idx - 1) + min_idx - 1
        else:
            return (n - max_idx - 1) + min_idx





        