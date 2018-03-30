# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        if m == 0:
            return False

        n = len(board[0])
        if n == 0:
            return False

        if len(word) == 0:
            return False

        self.board = board
        self.result = False
        self.solve('', '', m, n, word)
        return self.result

    def solve(self, x, y, m, n, word):
        if len(word) == 0:
            self.result = True
            return

        if x == '':
            # start
            for i in range(m):
                for j in range(n):
                    if self.board[i][j] == word[0]:
                        bak = word[0]
                        self.board[i][j] = '*'
                        self.solve(i, j, m, n, word[1:])
                        if self.result:
                            return
                        self.board[i][j] = bak
        else:
            # up
            if x - 1 >= 0 and self.board[x - 1][y] == word[0]:
                bak = word[0]
                self.board[x - 1][y] = '*'
                self.solve(x - 1, y, m, n, word[1:])
                if self.result:
                    return
                self.board[x - 1][y] = bak

            # right
            if y + 1 < n and self.board[x][y + 1] == word[0]:
                bak = word[0]
                self.board[x][y + 1] = '*'
                self.solve(x, y + 1, m, n, word[1:])
                if self.result:
                    return
                self.board[x][y + 1] = bak

            # down
            if x + 1 < m and self.board[x + 1][y] == word[0]:
                bak = word[0]
                self.board[x + 1][y] = '*'
                self.solve(x + 1, y, m, n, word[1:])
                if self.result:
                    return
                self.board[x + 1][y] = bak

            # left
            if y - 1 >= 0 and self.board[x][y - 1] == word[0]:
                bak = word[0]
                self.board[x][y - 1] = '*'
                self.solve(x, y - 1, m, n, word[1:])
                if self.result:
                    return
                self.board[x][y - 1] = bak


if __name__ == '__main__':
    solution = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = 'ABCB'
    print solution.exist(board, word)
