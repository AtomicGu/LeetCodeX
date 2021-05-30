from math import gcd

N = int(input())
A = [int(input()) for i in range(N)]

if N == 1:
    if A[0] != 1:
        print("INF")
    else:
        print(0)
    exit()

cd = A[0]
min_ = sorted([A[0], A[1]])
for i in A:
    cd = gcd(cd, i)
    if i < min_[0]:
        min_ = [i, min_[0]]
    elif i < min_[1]:
        min_ = [min_[0], i]

if cd != 1:
    print("INF")
    exit()

size = min_[0] * min_[1] + 1
nums = [True] * size
nums[0] = False
for i in A:
    nums[i] = False
    j = 1
    while i + j < size:
        if nums[j] is False:
            nums[i + j] = False
        j += 1

print(sum(nums))
