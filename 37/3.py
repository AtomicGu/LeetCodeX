from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col_sets = [[True for i in range(9)] for i in range(9)]
        row_sets = [[True for i in range(9)] for i in range(9)]
        sqr_sets = [[True for i in range(9)] for i in range(9)]

        def mark_point(x: int, y: int, i: int) -> None:
            col_sets[x][i] = False
            row_sets[y][i] = False
            sqr_sets[x // 3 * 3 + y // 3][i] = False
            # 实际上计算的过程与棋盘一点关系都没有，只与这三个约束列表有关
            return

        def recycle_point(x: int, y: int, i: int) -> None:
            col_sets[x][i] = True
            row_sets[y][i] = True
            sqr_sets[x // 3 * 3 + y // 3][i] = True
            # board[x][y] = None
            return

        def check_point(x: int, y: int, i: int) -> bool:
            return col_sets[x][i] and row_sets[y][i] and sqr_sets[x // 3 * 3 +
                                                                  y // 3][i]

        blanks = []
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char == ".":
                    blanks.append((x, y))
                else:
                    mark_point(x, y, int(char) - 1)

        stack = []

        def foo() -> bool:
            if len(stack) == len(blanks):
                return True

            x, y = blanks[len(stack)]
            for i in range(9):
                if check_point(x, y, i):
                    stack.append(i)
                    mark_point(x, y, i)
                    if foo():
                        return True
                    stack.pop()
                    recycle_point(x, y, i)

            return False

        if not foo():
            return

        for xy, v in zip(blanks, stack):
            x, y = xy
            board[x][y] = str(v + 1)

        return


s = Solution()
board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s.solveSudoku(board)

for i in range(9):
    print(board[i])
