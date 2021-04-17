# import sys
# import io
#
# sys.stdin = io.StringIO("""12345678.
# 123.46758
# """)

from array import array
from copy import copy


def xy(x, y):
    return x * 3 + y


class Grid9:
    def __init__(self, init=[0] * 9):
        self.grid = array("B", init)
        return

    def __hash__(self):
        ite = iter(self.grid)
        n = next(ite)
        for i in ite:
            n = (n << 8) | i
        return n

    def __repr__(self) -> str:
        return repr(self.grid)

    def __eq__(self, other):
        return hash(self) == hash(other)

    @staticmethod
    def from_string(s) -> "Grid9":
        g9 = Grid9()
        for i, j in enumerate(s):
            g9.grid[i] = 0 if "." == j else int(j)
        return g9

    def find_zero(self):
        for x in range(3):
            for y in range(3):
                if self.grid[x * 3 + y] == 0:
                    return x, y
        return

    def move_left(self, x, y):
        if y == 0:
            return
        init = copy(self.grid)
        init[xy(x, y)], init[xy(x, y - 1)] = init[xy(x, y - 1)], init[xy(x, y)]
        return Grid9(init), (x, y - 1)

    def move_right(self, x, y):
        if y == 2:
            return
        init = copy(self.grid)
        init[xy(x, y)], init[xy(x, y + 1)] = init[xy(x, y + 1)], init[xy(x, y)]
        return Grid9(init), (x, y + 1)

    def move_up(self, x, y):
        if x == 0:
            return
        init = copy(self.grid)
        init[xy(x, y)], init[xy(x - 1, y)] = init[xy(x - 1, y)], init[xy(x, y)]
        return Grid9(init), (x - 1, y)

    def move_down(self, x, y):
        if x == 2:
            return
        init = copy(self.grid)
        init[xy(x, y)], init[xy(x + 1, y)] = init[xy(x + 1, y)], init[xy(x, y)]
        return Grid9(init), (x + 1, y)


from queue import deque

start = Grid9.from_string(input())
target = Grid9.from_string(input())

searched = set()
bfs_queue = deque([(start, 0, start.find_zero())])
while bfs_queue:
    m, step, (x, y) = bfs_queue.popleft()

    if m == target:
        print(step)
        break

    if m in searched:
        continue
    searched.add(m)

    for f in [m.move_left, m.move_up, m.move_right, m.move_down]:
        _ = f(x, y)
        if _:
            t, xy_ = _
            bfs_queue.append((t, step + 1, xy_))

else:
    print(-1)
