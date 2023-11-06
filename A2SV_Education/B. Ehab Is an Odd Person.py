n = int(input())
nums = list(map(int, input().split()))
 
even = odd = False
 
for num in nums:
    if num % 2 == 0:
        even = True
    else:
        odd = True
        
nums.sort() if even and odd else nums
print(*nums)
