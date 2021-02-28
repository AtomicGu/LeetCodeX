N = int(input())

nums = []
for i in range(N):
    nums.extend(map(int, input().split()))

nums.sort()

for i in range(2, len(nums)):
    a = nums[i]
    b = nums[i - 1]
    if a != b + 1:
        if a == b:
            chongfu = a
        else:
            break_num = b + 1

print(break_num, chongfu)
