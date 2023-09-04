def solve():
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    dif = []

    for i in range(n):
        dif.append((y[i] - x[i], i))

    dif.sort(reverse=True)

    j = n - 1
    cnt = 0

    for i in range(n):
        while j > i and dif[i][0] + dif[j][0] < 0:
            j -= 1
        if j <= i:
            break
        cnt += 1
        j -= 1

    print(cnt)

t = int(input())
for _ in range(t):
    solve()
