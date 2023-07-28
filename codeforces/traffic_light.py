from typing import List

def traffic_light(val: str, sym: str) -> int:
    
    val = val.split(" ")
    char = val[1]

    sym += sym
    count = 0
    max_ = 0
    idx = 0

    while idx < len(sym):
        if sym[idx] == char:
            count = 0

            while idx < len(sym) and sym[idx] != "g":
                count += 1
                idx += 1

            if count > max_:
                max_ = count

        idx += 1
    return max_

t = int(input())

for _ in range(t):
    val = input()
    sym = input()

    print(traffic_light(val, sym))
