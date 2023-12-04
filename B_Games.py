#B. Games - Codeforces
   
from collections import defaultdict 
n = int(input())
hset = set()
nums = []
hmap = defaultdict(int)

for _ in range(n):
    h, a = map(int, input().split())
    hset.add(h)
    hmap[h] += 1
    nums.append(a)
 
res = 0   
for num in nums:
    if num in hset:
        res += hmap[num]
        
print(res)
        
        
    
    
    
    
    
    
        
        
    
    
    
    
    
       
    
    


    
    
    
    
    
    
    


    
    
    
    