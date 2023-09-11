import sys

INF = 10 ** 9 + 7

def solve():
    n = int(input())
    minn = INF
    min2 = []
    
    for _ in range(n):
        m = int(input())
        v = list(map(int, input().split()))
        minel = min(v)
        minn = min(minn, minel)
        v.remove(minel)
        min2.append(min(v))
    
    result = minn + sum(min2) - min(min2)
    print(result)

def main():
    # Uncomment this section if you want to read from a file
    # with open("a.in", "r") as f:
    #     sys.stdin = f
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
