from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def calc_possible_numbers(x: int, y: int) -> Set[str]:
            s = {str(i) for i in range(1, 10)}
            for i in range(0, 9):
                s.discard(board[x][i])
                s.discard(board[i][y])
            x0 = x // 3 * 3
            y0 = y // 3 * 3
            for i in range(x0, x0 + 3):
                for j in range(y0, y0 + 3):
                    s.discard(board[x][i])
            return s

        blanks = []
        for x in range(9):
            for y in range(9):
                if board[x][y] == ".":
                    blanks.append((x, y))

        def decide(n: int = 0) -> bool:
            if n >= len(blanks):
                return True

            x, y = blanks[n]
            s = calc_possible_numbers(x, y)
            # HACK 可以优化！
            # 不必在每个点上都重新计算该点处的可取值
            # 我们可以为每行、每列、每3x3区域都维护一个集合，存放候选数
            # 那么每次计算一个点处的候选值，只要把这几个集合取交就行了！
            for i in s:
                board[x][y] = i
                if decide(n + 1):
                    return True

            board[x][y] = "."
            return False

        decide()
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
