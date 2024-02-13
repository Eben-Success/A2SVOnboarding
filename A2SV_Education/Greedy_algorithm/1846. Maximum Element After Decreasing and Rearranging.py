class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)

        print(arr)
        if arr[0] > 1:
            arr[0] = 1

        for i in range(1, n):
            if abs(arr[i - 1] - arr[i]) > 1:
                arr[i] = arr[i-1] + 1 

        return arr[-1]
            


        
