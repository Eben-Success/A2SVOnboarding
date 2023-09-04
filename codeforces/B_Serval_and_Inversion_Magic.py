from collections import defaultdict

hashmap = defaultdict(int)

t = int(input())
ones, zeros = 0, 0
for _ in range(t):
    n = int(input())
    arr = list(map(int, input()))
    

    for num in arr:
        hashmap[num] += 1

    print(hashmap)  

    
    
