class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        n = len(letters)

        if letters[-1] < target:
            return letters[0]

        low, high = 0, n - 1

        while (low <= high):
            mid = (low + high) // 2

            if letters[mid] > target:
                high = mid - 1

            elif letters[mid] < target:
                low = mid + 1

            else:

                idx = mid + 1
                while idx < n and letters[mid] == letters[idx]:
                    idx += 1

                return letters[idx] if idx < n else letters[0]


        return letters[low]
        