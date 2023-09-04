t = int(input())
counter = 0
res_lst = []

while counter < t:
  counter += 1
  n, k = map(int, input().split())
  arr = list(map(int, input().split()))

  if k == 1:
    flag = 1

  else:
    flag = 1
    prev = arr[k-1] - arr[k-2]

    for i in range(k-2, 0, -1):
      if (arr[i] - arr[i-1]) > prev:
        flag = 0
        break
      prev = arr[i] - arr[i-1]

    if (arr[0] / (n-k+1)) > (arr[1] - arr[0]):
      flag = 0

  if flag:
    res_lst.append('Yes')

  else:
    res_lst.append('No')

integer_strings = map(str, res_lst)
result = "\n".join(integer_strings)
print(result)