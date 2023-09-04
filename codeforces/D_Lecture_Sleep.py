n, k = map(int, input().split())

a = list(map(int, input().split()))
t = list(map(int, input().split()))

total = 0

pr = [0] * n
for i in range(n):
    if i > 0:
        pr[i] += pr[i - 1]
    if t[i] == 0:
        pr[i] += a[i]
    else:
        total += a[i]

add = 0
for i in range(k - 1, n):
    add = max(add, pr[i] - (pr[i - k] if i >= k else 0))

print(total + add)
