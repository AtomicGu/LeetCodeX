# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

from pprint import pprint

N = int(input())
n = N // 2 + 1
mat = [[0 for j in range(N)] for i in range(N)]
for i in range(n):
    nums = list(map(int, input().split()))
    for j in range(i + 1):
        mat[i - j][j] = nums[j]
for i in range(n, N):
    nums = list(map(int, input().split()))
    for j in range(i - n + 1, n):
        mat[i - j][j] = nums[j]

for i in range(N - 2, -1, -1):
    for j in range(i + 1):
        right = mat[i - j][j + 1]
        bottom = mat[i - j + 1][j]
        mat[i - j][j] += max(right, bottom)

print(mat[0][0])
