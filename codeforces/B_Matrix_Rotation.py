
t = int(input())

for _ in range(t):
    mat = []
    row1 = list(map(int, input().split()))
    for num in row1:
        mat.append(num)
    row2 = list(map(int, input().split()))
    for num in row2:
        mat.append(num)

    min_elem, max_elem = min(mat), max(mat)

    min_idx, max_idx = mat.index(min_elem), mat.index(max_elem)

    if min_idx + max_idx == 3:
        print("YES")

    else:
        print("NO")



