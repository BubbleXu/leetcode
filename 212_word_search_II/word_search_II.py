# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Example:
#
# Input:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# Output: ["eat","oath"]
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.


class TireNode(object):
    def __init__(self):
        self.word = None
        self.children = {}


class Solution(object):
    def find_words(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        if m == 0:
            return []

        n = len(board[0])
        if n == 0:
            return []

        root = self.build_tire_tree(words)
        self.board = board
        self.result = []
        for i in range(m):
            for j in range(n):
                self.solve(i, j, m, n, root)
        return self.result

    def build_tire_tree(self, words):
        root = TireNode()
        for word in words:
            cur = root
            for c in word:
                if not cur.children.get(c):
                    cur.children[c] = TireNode()
                cur = cur.children[c]
            cur.word = word
        return root

    def solve(self, x, y, m, n, cur_node):
        c = self.board[x][y]
        if c == '*' or not cur_node.children.get(c):
            return
        cur = cur_node.children[c]
        if cur.word:
            self.result.append(cur.word)
            cur.word = None

        self.board[x][y] = '*'
        if x > 0:
            self.solve(x - 1, y, m, n, cur)
        if y > 0:
            self.solve(x, y - 1, m, n, cur)
        if x < m - 1:
            self.solve(x + 1, y, m, n, cur)
        if y < n - 1:
            self.solve(x, y + 1, m, n, cur)
        self.board[x][y] = c


if __name__ == '__main__':
    solution = Solution()
    board = [
      ['o','a','a','n'],
      ['e','t','a','e'],
      ['i','h','k','r'],
      ['i','f','l','v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print solution.find_words(board, words)