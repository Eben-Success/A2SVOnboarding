t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    
    a = input()
    b = input()
    
    a = sorted(a)
    b = sorted(b)
    c = []
    
    n_a = len(a)
    n_b = len(b)
    
    i, j = 0, 0
    a_cnt, b_cnt = 0, 0
    
    while i < n_a and j < n_b:
        if a[i] <= b[j] and a_cnt < k:
            c.append(a[i])
            i += 1
            a_cnt += 1
            b_cnt = 0
            
        if a[i] <= b[i] and a_cnt == k:
            c.append(b[j])
            a_cnt = 0
            j += 1
            b_cnt += 1
            
    print("".join(c))
        
    
    
    