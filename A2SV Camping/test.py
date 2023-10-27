
n = int(input())
times = list(map(int, input().split()))

alice, bob = 0, 0
aliceCnt, bobCnt = 0, 0
i, j = 0, n - 1

while i <= j:
    if aliceSpend <= bobSpend:
        aliceSpend += times[i]
        aliceCnt += 1
        i += 1
    else:
        bobSpend += times[j]
        bobCnt += 1
        j -= 1

print(aliceCnt, bobCnt)

n = int(input())
nums = list(map(int, input().split()))

l, r = 0, n - 1

alice = nums[l]
bob = nums[r]

alice_count = 0
bob_count = 0

while l <= r:
    if alice > bob:
        r -= 1
        bob += nums[r]
        bob_count += 1
        
    elif bob >= alice:
        l += 1
        alice += nums[l]
        alice_count += 1

print(alice_count, bob_count)
        

