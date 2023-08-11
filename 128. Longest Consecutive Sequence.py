class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # O(n)

        # if not nums: return 0

        hashset = set(nums)
        max_cons = 0

        for num in nums:
            if num - 1 not in hashset:
                # cur_num = num
                count = 1

                while num + 1 in hashset:
                    count += 1
                    num += 1

                max_cons = max(max_cons, count)

        return max_cons

        #  # Time: O(nlogn)

        if len(nums) == 0:
            return 0

        nums.sort()
        smallest = nums[0]
        count = 1
        max_cons = 1

        for i in range(len(nums)):
            if nums[i] - 1 == smallest:
                count += 1
                smallest = nums[i]


            elif smallest != nums[i]:
                count = 1
                smallest = nums[i]

            max_cons = max(max_cons, count)

        return max_cons
