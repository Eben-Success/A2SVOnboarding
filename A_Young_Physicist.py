n = int(input())
res = 0

x_sum = 0
y_sum = 0
z_sum = 0
for _ in range(n):
    x, y, z = map(int, input().split())
    x_sum += x
    y_sum += y
    z_sum += z
    
if x_sum == y_sum == z_sum == 0:
    print("YES")
else:
    print("NO")
    