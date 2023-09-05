class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        avg = float("-inf")
        cur_sum = 0
        l = 0

        for i in range(k):
            cur_sum += nums[i]

        avg = max(avg, (cur_sum/k))

        for i in range(k, len(nums)):
            cur_sum += nums[i]
            cur_sum -= nums[l]

            avg = max(avg, (cur_sum/k))
            l += 1

        return avg

        