t = int(input())

for _ in range(t):
    num_1, num_2, num_3 = list(map(int, input().split()))
    min_cost = float("inf")
    
    for num_a in [num_1 - 1, num_1, num_1 + 1]:
        for num_b in [num_2 - 1, num_2, num_2 + 1]:
            for num_c in [num_3 - 1, num_3, num_3 + 1]:
                cost = abs(num_a - num_b) + abs(num_a - num_c) + abs(num_b - num_c)
                min_cost = min(min_cost, cost)
                
    print(min_cost)
