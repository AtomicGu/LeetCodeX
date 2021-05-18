from typing import List
from pprint import pprint


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [[0] * n for i in range(n)]

        def place_at(x, y):
            for i in range(n):
                grid[x][i] += 1
                grid[i][y] += 1
            for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
                grid[i][j] += 1
            for i, j in zip(range(x, -1, -1), range(y, n, 1)):
                grid[i][j] += 1
            for i, j in zip(range(x, n, 1), range(y, -1, -1)):
                grid[i][j] += 1
            for i, j in zip(range(x, n, 1), range(y, n, 1)):
                grid[i][j] += 1
            return

        def remove_at(x, y):
            for i in range(n):
                grid[x][i] -= 1
                grid[i][y] -= 1
            for i, j in zip(range(x, -1, -1), range(y, -1, -1)):
                grid[i][j] -= 1
            for i, j in zip(range(x, -1, -1), range(y, n, 1)):
                grid[i][j] -= 1
            for i, j in zip(range(x, n, 1), range(y, -1, -1)):
                grid[i][j] -= 1
            for i, j in zip(range(x, n, 1), range(y, n, 1)):
                grid[i][j] -= 1
            return

        solutions = []

        def place_nth_queen(n_=0):
            if n_ == n:
                sln = []
                for row in grid:
                    sln.append("".join(["." if i == 0 else "Q" for i in row]))
                solutions.append(sln)
                return
            for x in range(n):
                for y in range(n):
                    if grid[x][y] == 0:
                        place_at(x, y)
                        place_nth_queen(n_ + 1)
                        remove_at(x, y)
            return

        place_nth_queen()
        return solutions


sln = Solution()
ans = sln.solveNQueens(8)
pprint(ans)
