from typing import List, Set


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col_sets = [{str(i) for i in range(1, 10)} for i in range(9)]
        row_sets = [{str(i) for i in range(1, 10)} for i in range(9)]
        sqr_sets = [{str(i) for i in range(1, 10)} for i in range(9)]
        # HACK 注意到，这里集合只可能是集合{1，2，3，4，5，6，7，8，9}的子集，是有限的
        # 所以可以用List[bool]进一步优化!

        def calc_possible_numbers(x: int, y: int) -> Set[str]:
            return col_sets[x].intersection(row_sets[y].intersection(
                sqr_sets[x // 3 * 3 + y // 3]))

        def put_point(x: int, y: int, char: str) -> None:
            col_sets[x].discard(char)
            row_sets[y].discard(char)
            sqr_sets[x // 3 * 3 + y // 3].discard(char)
            board[x][y] = char
            return

        def recycle_point(x: int, y: int) -> None:
            char = board[x][y]
            col_sets[x].add(char)
            row_sets[y].add(char)
            sqr_sets[x // 3 * 3 + y // 3].add(char)
            board[x][y] = "."
            return

        blanks = []
        for x in range(9):
            for y in range(9):
                char = board[x][y]
                if char == ".":
                    blanks.append((x, y))
                else:
                    put_point(x, y, char)

        def decide(n: int = 0) -> bool:
            if n >= len(blanks):
                return True

            x, y = blanks[n]
            s = calc_possible_numbers(x, y)
            for i in s:
                put_point(x, y, i)
                if decide(n + 1):
                    return True
                recycle_point(x, y)
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
