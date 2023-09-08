from typing import List

def rearrangeArray(nums: List[int]) -> List[int]:
    
    pos = [num for num in nums if num > 0]
    neg = [num for num in nums if num < 0]
    
    res = []
    
    for p, n in zip(pos, neg):
        res += [p, n]
        
    return res


nums = [3,1,-2,-5,2,-4, -6, -7, -77, -90]

print(rearrangeArray(nums))