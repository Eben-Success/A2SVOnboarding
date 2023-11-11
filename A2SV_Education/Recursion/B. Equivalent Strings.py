s1 = input()
s2 = input()

def isEquivalent(s1, s2, memo={}):
    if s1 == s2:
        return True
    
    if len(s1) % 2 == 1:
        return s1 == s2
    
    if (s1, s2) in memo:
        return memo[(s1, s2)]
    
    n = len(s1)
    a1 = s1[:n//2]
    a2 = s1[n//2:]
    b1 = s2[:n//2]
    b2 = s2[n//2:]
    
    memo[(s1, s2)] = (isEquivalent(a1, b1, memo) and isEquivalent(a2, b2, memo)) or (isEquivalent(a1, b2, memo) and isEquivalent(a2, b1, memo))
    return memo[(s1, s2)]

if isEquivalent(s1, s2):
    print("YES")
else:
    print("NO")
