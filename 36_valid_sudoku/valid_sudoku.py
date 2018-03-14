# Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


class Solution(object):
    def is_valid_sudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dict = {}
        # check line
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in dict:
                    return False
                else:
                    dict[board[i][j]] = True
            dict.clear()

        # check column
        for i in range(9):
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in dict:
                    return False
                else:
                    dict[board[j][i]] = True
            dict.clear()

        # check square
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                # start point (i, j)
                for m in [0, 1, 2]:
                    for n in [0, 1, 2]:
                        if board[i + m][j + n] != '.' and board[i + m][j + n] in dict:
                            return False
                        else:
                            dict[board[i + m][j + n]] = True
                dict.clear()

        return True


if __name__ == '__main__':
    solution = Solution()
    board = [[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
             ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
             ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
    print solution.is_valid_sudoku(board)
