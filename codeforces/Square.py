n = int(input())
 
for _ in range(n):
    rec_1 = list(map(int, input().split()))
    rec_2 = list(map(int, input().split()))
    
    
    rec1_len, rec1_wid = max(rec_1), min(rec_1)
    
    rec2_len, rec2_wid = max(rec_2), min(rec_2)
    
    if rec1_len == rec2_len and rec1_wid + rec2_wid == rec1_len:
        print("Yes")
    else:
        print("No")
