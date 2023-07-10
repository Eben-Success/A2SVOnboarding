class Solution:
    
    """
    Time: O(n^2) | Space: O(n)
    
    Algorithm
    1. Create a helper function to compare two strings at a time in nums.
    2. In the main function, convert int(num) to str(num)
    3. Call the helper function, if 1: swap them in place.
    4. stringify the entire nums.
    5. Move leading 0s.
    6. Return res
    """

    def compare_strings(self, x: str, y:str):
        xy = x + y
        yx = y + x
        
        if xy > yx:
            return -1 # y comes before x
        elif xy < yx:
            return 1 # x comes before y
        else:
            return 0

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
    
        # use two pointers to traverse the nums
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                # swap if compare_string == 1
                if self.compare_strings(nums[i], nums[j]) == 1:
                    nums[i], nums[j] = nums[j], nums[i]
                    
        # join sorted nums
        res = "".join(nums)
        
        # remove 0s in front of joined nums
        res = res.lstrip('0')
        
        return res if res else '0'

        

            