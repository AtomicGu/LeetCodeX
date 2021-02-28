m, n = list(map(int, input().split()))
mat = [None for i in range(n)]

total = 0
for i in range(n):
    t = list(map(int, input().split()))
    total += sum(t)
    mat[i] = t

if total % 2 == 1:
    print(0)
    exit()
total = total // 2

least = m * n


def search(i, j, grid_num, now_sum):
    global least
    if i >= n or j >= m or i < 0 or j < 0:  # 越界
        return
    x = mat[i][j]
    if x is None:
        return  # 搜过了
    grid_num += 1
    if grid_num >= least:  # 不可能更小了
        return
    t = now_sum + x
    if t > total:
        return  # 不可能更小了
    if t == total:
        least = grid_num
        return

    mat[i][j] = None
    search(i - 1, j, grid_num, t)
    search(i, j - 1, grid_num, t)
    search(i + 1, j, grid_num, t)
    search(i, j + 1, grid_num, t)
    mat[i][j] = x
    return


search(0, 0, 0, 0)
print(least)
