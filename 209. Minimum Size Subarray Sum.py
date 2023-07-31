from collections import deque

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Solution: 1

        Time: O(n) | Space: O(n)

        cur_sum = deque(nums[0])

        min_wind = float("inf")

        for i in range(1, len(nums)):
            cur_sum.append(nums[i])

            while sum(cur_sum) > target:
                cur_sum.popleft()

            min_wind = min(min_wind, len(cur_sum))

        return min_wind


        # Solution 2
        # Time: O(n) | Space: O(1)
        cur_sum = 0
        min_sum = float("inf")
        l = 0

        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target:
                cur_sum -= nums[l]
                min_sum = min(min_sum, r - l + 1)
                l += 1

        return 0 if min_sum == float("inf") else min_sum


        """
        Intuition to Soln 1
        Store the first elem in a queue.
        While sum(queue) > target:
        popleft from the queue.
        update min_wind
        return it.
        """

        """
        Intuition to Soln 2:
        use two pointers: l at 0 and r in for loop
        1. Get the 1st elem as min_window.
        2. Iterate over nums and add to min_window
        3. While min_window >= target:
        4. subtrate num[l]
        5. Update min_win and return it
        """


        


        

        
        

                   

        

