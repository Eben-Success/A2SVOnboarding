t = int(input())

for _ in range(t):
    s = input()
    res = []
    i = 0
    while i < len(s):
        if i + 1 < len(s) and s[i] == s[i+1]:
            i += 2
        else:
            res.append(s[i])
            i += 1
    res = sorted(set(res))
    print(''.join(res))