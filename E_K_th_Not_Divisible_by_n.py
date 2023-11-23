t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    num = 1
    while k > 0 and True:
        if num % n != 0:
            k -= 1
            num += 1
            
        
    print(num)
    