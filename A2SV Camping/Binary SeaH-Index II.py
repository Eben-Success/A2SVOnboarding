class Solution:
    def hIndex(self, citations: List[int]) -> int:

        # Implement bisect left

        # Time: O(logn) | Space: O(1)
        n = len(citations)
        left, right = 0, n - 1
        h_index = 0

        while left <= right:
            mid = (left + right) // 2

            if citations[mid] >= n - mid:
                h_index = n - mid
                right = mid - 1

            else:
                left = mid + 1
        return h_index
