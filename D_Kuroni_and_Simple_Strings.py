s = input()
n = len(s)

open_bracket, close_bracket = [], []

res = []

for i in range(n):
    if s[i] == "(": open_bracket.append(i)
        
    if s[i] == ")": close_bracket.append(i)
    
n_open = len(open_bracket)
n_close = len(close_bracket)

left, right = 0, n_close - 1

while left < n_open and right >= 0:
    if open_bracket[left] > close_bracket[right]: break
    
    res.append(open_bracket[left])
    res.append(close_bracket[right])
    left += 1
    right -= 1
    
n_res = len(res)

res.sort()

if n_res == 0: print(0)

else:
    indexes = [idx + 1 for idx in res]
    print(1)
    print(n_res)
    print(*indexes)