class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        n = len(nums)
        second_num = float("-inf")

        """
        2 3 1
        stack = 1, 3
        """

        for i in range(n - 1, -1, -1):
            if nums[i] < second_num:
                return True

            while stack and stack[-1] < nums[i]:
                second_num = stack.pop()
                
            stack.append(nums[i])

        return False
        
