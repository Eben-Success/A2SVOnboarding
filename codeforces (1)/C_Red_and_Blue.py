t = int(input())

for _ in range(t):
    n = int(input())
    nums1 = list(map(int, input().split()))
    m = int(input())
    nums2 = list(map(int, input().split()))
    
    prefix_1 = [0] * (n + 1)
    prefix_2 = [0] * (m + 1)
    
    for i in range(1, (n + 1)):
        prefix_1[i] = prefix_1[i-1] + nums1[i-1]
        
        
    for i in range(1, (m + 1)):
        prefix_2[i] = prefix_2[i-1] + nums2[i-1]   
    
    print(max(prefix_1) + max(prefix_2))