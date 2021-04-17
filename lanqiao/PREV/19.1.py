# import sys
# import io
#
# sys.stdin = io.StringIO("""12345678.
# 123.46758
# """)


def string2matrix(s):
    return [[
        0 if "." == s[i * 3 + j] else int(s[i * 3 + j]) for j in range(3)
    ] for i in range(3)]


a = string2matrix(input())
b = string2matrix(input())


def frozen_matrix(m):
    return tuple([tuple(i) for i in m])


def unfrozen_matrix(m):
    return list([list(i) for i in m])


def find_zero(m):
    for x in range(3):
        for y in range(3):
            if m[x][y] == 0:
                return x, y
    return None


def move_left(m):
    x, y = find_zero(m)
    if y == 0:
        return False
    m[x][y - 1], m[x][y] = m[x][y], m[x][y - 1]
    return True


def move_up(m):
    x, y = find_zero(m)
    if x == 0:
        return False
    m[x - 1][y], m[x][y] = m[x][y], m[x - 1][y]
    return True


def move_right(m):
    x, y = find_zero(m)
    if y == 2:
        return False
    m[x][y + 1], m[x][y] = m[x][y], m[x][y + 1]
    return True


def move_down(m):
    x, y = find_zero(m)
    if x == 2:
        return False
    m[x + 1][y], m[x][y] = m[x][y], m[x + 1][y]
    return True


from queue import deque

start = frozen_matrix(a)
target = frozen_matrix(b)
bfs_queue = deque([(start, 0)])

searched = set()
while bfs_queue:
    m, step = bfs_queue.popleft()

    if m == target:
        print(step)
        break

    if m in searched:
        continue
    searched.add(m)

    for f in [move_left, move_up, move_right, move_down]:
        a = unfrozen_matrix(m)
        if f(a):
            bfs_queue.append((frozen_matrix(a), step + 1))

else:
    print(-1)
