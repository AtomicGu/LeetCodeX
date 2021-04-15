from typing import *
from collections import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def bfs(x, y):
            queue = deque([(x, y)])
            while queue:
                x, y = queue.popleft()
                if not 0 <= x < m or not 0 <= y < n:
                    continue
                if board[x][y] == "O":
                    board[x][y] = "Y"
                    queue.append((x - 1, y))
                    queue.append((x + 1, y))
                    queue.append((x, y - 1))
                    queue.append((x, y + 1))
            return

        for i in range(m):
            bfs(i, 0)
            bfs(i, n - 1)
        for j in range(n):
            bfs(0, j)
            bfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "Y":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
        return


sln = Solution()
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
sln.solve(board)
print(board)
