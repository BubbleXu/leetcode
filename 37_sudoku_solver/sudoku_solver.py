# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# Empty cells are indicated by the character '.'.
#
# You may assume that there will be only one unique solution.

class Solution(object):
    def solve_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.left = []
        self.row_dict = [{} for _ in range(9)]
        self.col_dict = [{} for _ in range(9)]
        self.square_dict = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    self.left.append((i, j))
                else:
                    self.row_dict[i][board[i][j]] = True
                    self.col_dict[j][board[i][j]] = True
                    self.square_dict[i / 3 * 3 + j / 3][board[i][j]] = True

        self.solve(board)

    def solve(self, board):
        if len(self.left) == 0:
            return

        # get current left point
        i, j = self.left.pop()

        # check candidate numbers
        candidate = []
        for k in range(1, 10):
            key = str(k)
            if self.row_dict[i].get(key) is None \
                    and self.col_dict[j].get(key) is None \
                    and self.square_dict[i / 3 * 3 + j / 3].get(key) is None:
                candidate.append(key)

        for k in candidate:
            board[i][j] = k
            self.row_dict[i][k] = True
            self.col_dict[j][k] = True
            self.square_dict[i / 3 * 3 + j / 3][k] = True
            self.solve(board)

            if len(self.left) == 0:
                return
            else:
                board[i][j] = '.'
                self.row_dict[i].pop(k)
                self.col_dict[j].pop(k)
                self.square_dict[i / 3 * 3 + j / 3].pop(k)

        self.left.append((i, j))


if __name__ == '__main__':
    solution = Solution()
    board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
             [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
             [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
             [".", ".", ".", "2", "7", "5", "9", ".", "."]]

    solution.solve_sudoku(board)
    print board
