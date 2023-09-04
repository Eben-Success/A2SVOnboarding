# C. Kuriyama Mirai's Stones

def Solution():
    n = int(input())

    nums = list(map(int, input().split()))
    
    sorted_nums = sorted(nums)

    m = int(input())
    
    prefix = [0] * (n + 1)
    sorted_pre = [0] * (n + 1)
       
    
    for i in range(n):
        prefix[i+1] = nums[i] + prefix[i]
        sorted_pre[i+1] = sorted_nums[i] + sorted_pre[i]        

        

    for _ in range(m):
        q, l , r = list(map(int, input().split()))
        
        res = 0
        if q == 1:
            # res += prefix[r] - prefix[l-1]  
            print(prefix[r] - prefix[l-1])
        else:
            # res += sorted_pre[r] - sorted_pre[l-1]
            print(sorted_pre[r] - sorted_pre[l-1])
            
                
        
Solution()
        
        
    

    
    
    
    
