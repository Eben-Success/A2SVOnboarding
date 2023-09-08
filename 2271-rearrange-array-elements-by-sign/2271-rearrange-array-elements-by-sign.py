class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        # pos = [num for num in nums if num > 0]
        # neg = [num for num in nums if num < 0]

        # res = []

        # for p, n in zip(pos, neg):
        #     res += [p, n]

        # return res

        n = len(nums)
        res = [0] * n

        left, right = 0, 1

        for num in nums:
            if num > 0:
                res[left] = num
                left += 2

            else:
                res[right] = num
                right += 2
        return res
        
        