t = int(input())

for _ in range(t):
    n = int(input())
    cubes = list(map(int, input().split()))
    
    check = False
    for i in range(1, n):
        if cubes[i] >= cubes[i-1]:
            check = True
            break
        
    if check:
        print("YES")
    else:
        print("NO")
