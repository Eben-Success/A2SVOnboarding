str_a = input()
str_b = input()

n = len(str_a)
mid = n // 2

a1 = str_a[:mid]
a2 = str_a[mid:]

b1 = str_b[:mid]
b2 = str_b[mid:]

sa1 = set(a1)
sa2 = set(a2)
sb1 = set(b1)
sb2 = set(b2)

even = False


flag = False
if sa1 == sb2  and sa2 == sb1:
    print("YES")
    flag = True
    
elif sa1 == sb1 and sa2 == sb2:
    print("YES")
    flag = True
    
if not flag:
    print("NO")
    