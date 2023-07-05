n = int(input())
values = list(map(int, input().split()))

pos, neg, zero = [], [], []

for elem in values:
    if elem < 0:
        neg.append(elem)
    elif elem > 0:
        pos.append(elem)
    else:
        zero.append(elem)
        
if len(pos) == 0:
    pos.append(neg.pop())
    pos.append(neg.pop())
    
if len(neg) % 2 == 0:
    zero.append(neg.pop())
    
print(len(pos), *pos)
print(len(neg), *neg)
print(len(zero), *zero)
