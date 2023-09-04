n, q = map(int, input().split())
prices = list(map(int, input().split()))
prices.sort()
prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + prices[i]
    

for _ in range(q):
    x, y = map(int, input().split())
    print(prefix[n - x + y] - prefix[n - x])
