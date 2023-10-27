k = int(input())
count = 0

ans = 0
idx = 1
count = 0

while count < k:
    num = str(idx)
    cur_sum = 0
    for char in num:
        cur_sum += int(char)
    if cur_sum == 10:
        ans = idx
        count += 1
        
    idx += 1
print(ans)
        

    
    