# LUcky: Codeforces

t = int(input())

for _ in range(t):
    
    s = input()
    
    forward = 0
    for i in range(3):
        forward += int(s[i])
        
    backward = 0
    for i in range(3, 6):
        backward += int(s[i])
    
    if forward == backward:
        print("YES")
    else:
        print("NO")
    
    
    
    
    