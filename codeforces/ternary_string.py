def ternary_string(s):
    char_count = {c: 0 for c in '123'}
    min_sub = float("inf")
    l = 0
 
    for r in range(len(s)):
        char_count[s[r]] += 1
 
        while all(char_count[c] > 0 for c in '123'):
            min_sub = min(min_sub, r - l + 1)
            char_count[s[l]] -= 1
            l += 1
 
    return 0 if min_sub == float("inf") else min_sub
 
 
t = int(input())
 
for _ in range(t):
    s = input()
    print(ternary_string(s))
