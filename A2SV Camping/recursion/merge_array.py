
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

nums1 = [1, 2, 3, 4]
nums2 = [2, 3, 4, 5,6 , 7, 8, 8, 9]

print(merge(nums1, nums2))
        
            
        