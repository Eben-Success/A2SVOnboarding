class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        count = 0
        n = len(nums)
        hashmap = {0: 1}
        prefix_sum = 0

        for num in nums:
            prefix_sum += num

            remainder = prefix_sum % k

            if remainder in hashmap:
                count += hashmap[remainder]

            hashmap[remainder] = 1 + hashmap.get(remainder, 0)

        return count
        