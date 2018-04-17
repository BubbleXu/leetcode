# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m <= 2:
            return

        n = len(board[0])
        if n <= 2:
            return

        queue = []
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = '#'
                    queue.append((i, j))

        for j in [0, n - 1]:
            for i in range(1, m - 1):
                if board[i][j] == 'O':
                    board[i][j] = '#'
                    queue.append((i, j))

        while queue:
            i, j = queue.pop(0)
            # up
            if i - 1 >= 0 and board[i - 1][j] == 'O':
                board[i - 1][j] = '#'
                queue.append((i - 1, j))

            # right
            if j + 1 < n and board[i][j + 1] == 'O':
                board[i][j + 1] = '#'
                queue.append((i, j + 1))

            # down
            if i + 1 < m and board[i + 1][j] == 'O':
                board[i + 1][j] = '#'
                queue.append((i + 1, j))

            # left
            if j - 1 >= 0 and board[i][j - 1] == 'O':
                board[i][j - 1] = '#'
                queue.append((i, j - 1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == '__main__':
    solution = Solution()
    board = [["X", "O", "X", "X"], ["O", "X", "O", "X"], ["X", "O", "X", "O"], ["O", "X", "O", "X"],
             ["X", "O", "X", "O"], ["O", "X", "O", "X"]]
    solution.solve(board)
