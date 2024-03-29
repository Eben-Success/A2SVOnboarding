t = int(input())

for _ in range(t):
    n = int(input())
    robots = list(map(int, input().split()))
    
    max_robot = max(robots)
    cnt_robots = [0] * (max_robot + 1)
    
    for num in robots:
        cnt_robots[num] += 1
        
    for i in range(len(cnt_robots) - 1):
        if cnt_robots[i] < cnt_robots[i+1]:
            print("NO")
            break
    else:
        print("YES")
