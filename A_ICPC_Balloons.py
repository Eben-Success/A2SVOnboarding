
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(input())
    
    hset = set()
    count = 0
    for num in s:
        if num not in hset:
            count += 2
            hset.add(num)
        else:
            count += 1
            
    print(count)
        
        