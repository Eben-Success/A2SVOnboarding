import math

"""
find two numbers a and b that a^3 + b^3 = x
"""

t = int(input())

for _ in range(t):
    x = int(input())
        
    l, r = 1, int(pow(x, 1/3))
    
    ans = "NO"
    
    while l <= r:
        if l**3 + r**3 == x:
            ans = "YES"
            break
        
        elif l**3 + r**3 < x:
            l += 1
            
        elif l**3 + r**3 > x:
             r -= 1
             
    print(ans)
             
    