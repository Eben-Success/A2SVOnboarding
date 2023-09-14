class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = self.bisect_left(nums, target)
        last = self.bisect_right(nums, target)
        return [first, last]

    def bisect_left(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        leftmost = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                leftmost = mid
                high = mid - 1
        return leftmost


    def bisect_right(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        rightmost = -1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                rightmost = mid
                low = mid + 1
        return rightmost
