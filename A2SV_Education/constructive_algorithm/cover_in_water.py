t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    

    def solve(s):
        if "..." in s:
            return 2
        return s.count(".")
    
    print(solve(s))
