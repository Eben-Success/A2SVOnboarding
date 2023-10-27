
def merge(nums1, nums2):
    n1 = len(nums1)
    n2 = len(nums2)
    n = n1 + n2
    res = []
    
    l, r = 0, 0
    while l < n1 and r < n2:
        if nums1[l] < nums2[r]:
            res.append(nums1[l])
            l += 1
        elif nums1[l] > nums2[r]:
            res.append(nums2[r])
            r += 1
        else:
            res.append(nums1[l])
            res.append(nums2[r])
            l += 1
            r += 1 
    if n1 > n2:
        res.extend(nums1[l:])
    else:
        res.extend(nums2[r:])
    return res


from typing import List
def mergeSort(nums: List[int]) -> List[int]:
    
    if len(nums) <= 1:
        return nums
    
    mid = len(nums) // 2
    L = mergeSort(nums[:mid])
    R = mergeSort(nums[mid:])
    
    return merge(L, R)
    
    
nums = [4,6,3,2,6,7,8,9,10,11]
print(mergeSort(nums))
# nums1 = [1, 2, 3, 4]
# nums2 = [2, 3, 4, 5,6 , 7, 8, 8, 9]

# print(merge(nums1, nums2))
        
"""
i = k = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            nums[k] = L[i]
            i += 1
        else:
            nums[k] = R[j]
            j += 1
        k += 1
            
    while i < len(L):
        nums[k] = L[i]
        i += 1
        k += 1
        
    while j < len(R):
        nums[k] = R[j]
        j += 1
        k += 1
        
    return 
"""     
        