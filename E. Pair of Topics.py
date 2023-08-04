from typing import List

# # Optimal Approach | Time: O(nlogn)
def topic_pairs(n, teach: List[int], std: List[int]) -> int:

    res = []
    for i in range(n):
        res.append(teach[i] - std[i])
    res.sort()

    l, r = 0, n - 1
    count = 0

    while l < r:
        if res[l] + res[r] <= 0:
            l += 1
        else:
            count += r - l
            r -= 1
    return count


if __name__ == "__main__":
    n = int(input())
    teach = list(map(int, input().split()))
    std = list(map(int, input().split()))

    print(topic_pairs(n, teach, std))
