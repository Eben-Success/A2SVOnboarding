class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        arr = nums + [float("-inf")]
        res = 0
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= arr[mid + 1]:
                if arr[mid] > arr[mid + 1]:
                    res = mid
                high = mid - 1

            else:
                low = mid + 1

        return res
