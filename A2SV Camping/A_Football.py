s = input()

c_1 = 0
c_0 = 0
flag = False
for c in s:
    if c == "1":
        c_0 = 0
        c_1 += 1
        
        if c_1 >= 7:
            flag = True
            break
        
    if c == "0":
        c_1 = 0
        c_0 += 1
        
        if c_0 >= 7:
            flag = True
            break
        
if flag:
    print("YES")
else:
    print("NO")
        
    
    
    

