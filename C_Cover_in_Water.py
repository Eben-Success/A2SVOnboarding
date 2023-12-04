
from collections import defaultdict
t = int(input())


l = 0

for _ in range(t):
    hmap = defaultdict(int)
    count = 0
    three = False
    n = int(input())
    s = input()
        
    for r in range(n):
        if s[r] == ".":
            hmap[s[r]] += 1
            count += 1
            
            if count == 3:
                hmap["."] -= 3
                three = True
                break
        else:
            count = 0
  
    
    if three:      
        print(2)   
    else:
        print(sum(list(hmap.values())))