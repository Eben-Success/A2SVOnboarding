class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        n = len(height)
        left, right = 0, n - 1

        while left < right:
            diff = right - left 
            area = (min(height[left], height[right])) * diff
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1

            elif height[left] > height[right] :
                right -= 1

            else:
                right -= 1
                left += 1

        return max_area
        