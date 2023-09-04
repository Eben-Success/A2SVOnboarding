t = int(input())

for _ in range(t):
    
    arr = list(map(str, input()))
    
    arr.sort()
    
    print("".join(arr))