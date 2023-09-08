from typing import List

def increasingTripleft(nums: List[int]):
    
    first_num = second_num = float("inf")
    
    for num in nums:
        if num <= first_num:
            first_num = num
            
        elif num <= second_num:
            second_num = num
            
        else:
            return True
        
    return False



nums1 = [1,2,3,4,5]
nums2 = [5,4,3,2,1]
nums3 = [2,1,5,0,4,6]

print(increasingTripleft(nums1))
# print(increasingTripleft(nums2))
# print(increasingTripleft(nums3))