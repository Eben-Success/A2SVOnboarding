class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        # Naive Approach
        # Time: O(n) | Space: O(1)
        
        # idx = 0
        # while arr[idx] < arr[idx + 1]:
        #     idx += 1
        # return idx

        # O(logn)

        left, right = 0, len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left # you can return any pointer


        
