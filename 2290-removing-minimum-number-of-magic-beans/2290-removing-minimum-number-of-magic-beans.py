class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:

        beans.sort()
        res = []

        sum_ = sum(beans)
        n = len(beans)

        for i in range(n):
            res.append(sum_ - (beans[i] * (n - i)))

        return min(res)

        """
        Sort the array and use this formula.
        For: [4, 1, 6, 5]
        [1, 4, 5, 6]

        Get the sum - current elem * (# remaining element)
        """


        