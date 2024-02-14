class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        """
        [1,2,3]
        [1,3,2]
        [1,1,2,3]
        [1,2,1,3]
        [2,1,1,3]
        [2,3,1]
        [3,1,2]
        [3,2,1]

        [1,9,4,7,6]

        0. Always iterate from left
        1. Find first increase
        2. If occurences first the last occurence from left
        3. Smallest, the next number from left smaller than the first increase.

        large, small
        """
        n = len(arr)

        # find first increase from left
        first = [0, -1]
        for i in range(n - 1, 0 , -1):
            if arr[i-1] - arr[i] > 0:
                first[0] = arr[i-1]
                first[1] = i - 1
                break

        #find the second num less than first increase
        second = [0, -1]
        for i in range(n - 1, 0, -1):
            if arr[i] < first[0]:
                if arr[i-1] != arr[i]:
                    second[0] = arr[i]
                    second[1] = i
                    break


        arr[first[1]], arr[second[1]] = arr[second[1]], arr[first[1]]

        return arr
