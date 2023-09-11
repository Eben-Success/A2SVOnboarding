t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    l, r = 0, len(s) - 1
    count = 0
    
    while l <= r:
        if s[l] != s[r]:
            l += 1
            r -= 1
            
        elif s[l] == s[r]:
            count += r - l + 1
            break
            
    print(count)
    