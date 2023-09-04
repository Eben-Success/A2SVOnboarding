from collections import defaultdict

t = int(input())

for _ in range(t):
    n = int(input())
    
    nums = list(map(int, input().split()))
    
    """
    0 1 2 3 4 5 6
    
    6 0 3 3 6 7 2 7
    0 2 3 3 6 6 7 7
    
    

    hash = {0: 1, 2: 1, 3: 2, 6: 2, 7: 2}
    """
    
    hashmap = defaultdict(int)
    
    for num in nums:
        hashmap[num] += 1
        
    print(hashmap.values())
    
    