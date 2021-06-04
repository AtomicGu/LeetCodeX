mat = [
    [True, True, True, True, True, True],
    [True, False, False, False, False, True],
    [True, False, False, False, False, True],
    [True, False, False, False, False, True],
    [True, False, False, False, False, True],
    [True, True, True, True, True, True],
]

counter = 0


def dfs(x, y, k=0):
    global counter

    if mat[x][y]:
        return

    if k == 15:
        counter += 1
        return

    mat[x][y] = True

    k += 1
    dfs(x - 1, y, k)
    dfs(x + 1, y, k)
    dfs(x, y - 1, k)
    dfs(x, y + 1, k)

    mat[x][y] = False
    return


for x in range(1, 5):
    for y in range(1, 5):
        dfs(x, y)
print(counter)
