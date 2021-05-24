n = int(input())
nums = [[i, 0] for i in map(int, input().split())]

for i in range(n - 1):
    for j in range(n - i - 1):
        if nums[j][0] > nums[j + 1][0]:
            nums[j][1] += 1
            nums[j + 1][1] += 1
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

sum_ = 0
for _, a in nums:
    sum_ += (1 + a) * a // 2

print(sum_)

# 这题居然不是冒泡排序！
# 说是什么逆序数和树状数组，天哪，那（树状数组）是什么？
