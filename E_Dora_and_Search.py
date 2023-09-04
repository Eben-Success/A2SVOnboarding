
    
def Solve():
    n = int(input())
    
    nums = list(map(int, input().split()))
    
    left, right = 0, n - 1
    max_ = n
    min_ = 1
    
    flag = True
    
    while left < right:
        if nums[left] == max_ or nums[right] == max_:
            if nums[left] == max_:
                left += 1
            else:
                right -= 1
            max_ -= 1
        elif nums[left] == min_ or nums[right] == min_:
            if nums[right] == min_:
                right -= 1
            else:
                left += 1
            min_ += 1
        else:
            print(left + 1, right + 1)
            return
        
    print(-1)
        
        


t = int(input())

for _ in range(t):
    Solve()