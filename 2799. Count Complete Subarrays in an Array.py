from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        count = defaultdict(int)
        l = res = 0
        distinct = len(set(nums))
        n = len(nums)

        for r in range(n):
            count[nums[r]] += 1

            while len(count) == distinct:
                count[nums[l]] -= 1
                if count[nums[l]] == 0:
                    del count[nums[l]]

                res += n - r
                l += 1
        return res
        
