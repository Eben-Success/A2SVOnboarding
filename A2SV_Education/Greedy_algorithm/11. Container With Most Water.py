class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        n = len(height)
        l, r = 0, n - 1
        

        while l < r:
            length = min(height[l], height[r])
            width = (r - l)
            max_water = max(max_water, length * width)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_water
