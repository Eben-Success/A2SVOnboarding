n = int(input())

num = str(n)

arr = []

for char in num:
    arr.append(char)
    
res = []
for i in range(len(arr)):
    if i == 0:
        if arr[i] == '9':
            res.append(arr[i])
            continue
    if int(arr[i]) > 4:
        arr[i] = 9 - int(arr[i])
        arr[i] = str(arr[i])
        
    res.append(arr[i])

print(int("".join(res)))



 

    

        


