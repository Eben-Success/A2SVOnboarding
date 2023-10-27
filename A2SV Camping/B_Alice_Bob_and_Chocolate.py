n = int(input())
nums = list(map(int, input().split()))

alice, bob = 0, 0
alice_count, bob_count = 0, 0
l, r = 0, n - 1

while l <= r:
    if alice <= bob:
        alice += nums[l]
        alice_count += 1
        l += 1
    else:
        bob += nums[r]
        bob_count += 1
        r -= 1

print(alice_count, bob_count)