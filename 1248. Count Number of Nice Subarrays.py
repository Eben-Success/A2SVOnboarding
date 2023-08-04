class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # Time: O(n) | Space: O(1)

        res = count = odd_count = l = 0

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
                count = 0

                while odd_count == k:
                    if nums[l] % 2 == 1:
                        odd_count -= 1
                    l += 1
                    count += 1
            res += count

        return res
