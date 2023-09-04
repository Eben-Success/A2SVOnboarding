s = input()

n = int(input())

prefix = [0] * (len(s))
prefix[0] = 0

for i in range(1, len(prefix)): 
    if s[i] == s[i-1]:
        prefix[i] = prefix[i-1] + 1
    else:
        prefix[i] += prefix[i-1]

for _ in range(n):
    x, y = map(int, input().split())
    print(prefix[y-1] - prefix[x-1])
    
