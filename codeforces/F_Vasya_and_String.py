n, k = map(int, input().split())
arr = list(map(str, input()))

l, r = 0, 0

while r < n:
    if arr[r] != arr[l]:
        if k > 0:
            k -= 1
        else:
            while arr[l] == arr[l - 1]:
                l += 1
            l += 1
    r += 1

print(r - l)
