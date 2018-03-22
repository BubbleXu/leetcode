# coding: utf-8
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement,
# where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# For example,
# There exist two distinct solutions to the 4-queens puzzle:
#
# [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
import copy


class Solution(object):
    def solve_n_queens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        self.solve2([], [], [], n, result)
        return result

        # result = []
        # cur_result = [['.'] * n for _ in range(n)]
        # cur_occupy = copy.deepcopy(cur_result)
        # self.solve(0, cur_result, cur_occupy, result)
        # return result

    def solve(self, cur_row, cur_result, cur_occupy, result):
        n = len(cur_result)
        if cur_row == n:
            cur_result = [''.join(row) for row in cur_result]
            result.append(cur_result)
            return

        for i in range(n):
            if cur_occupy[cur_row][i] != '*':
                next_result = copy.deepcopy(cur_result)
                next_result[cur_row][i] = 'Q'

                next_occupy = copy.deepcopy(cur_occupy)
                for j in range(n):
                    next_occupy[cur_row][j] = '*'

                for j in range(cur_row + 1, n):
                    next_occupy[j][i] = '*'

                tmp_row = cur_row + 1
                tmp_col = i + 1
                while tmp_row < n and tmp_col < n:
                    next_occupy[tmp_row][tmp_col] = '*'
                    tmp_row += 1
                    tmp_col += 1

                tmp_row = cur_row + 1
                tmp_col = i - 1
                while tmp_row < n and tmp_col >= 0:
                    next_occupy[tmp_row][tmp_col] = '*'
                    tmp_row += 1
                    tmp_col -= 1

                self.solve(cur_row + 1, next_result, next_occupy, result)

    # In this problem, whenever a location (x, y) is occupied,
    # any other locations (p, q) where p + q == x + y or p - q == x - y would be invalid.
    def solve2(self, cur_result, xy_dif, xy_sum, n, result):
        p = len(cur_result)
        if p == n:
            result.append(['.' * i + 'Q' + '.' * (n - i - 1) for i in cur_result])
            return

        for q in range(n):
            if q not in cur_result and p - q not in xy_dif and p + q not in xy_sum:
                self.solve2(cur_result + [q], xy_dif + [p - q], xy_sum + [p + q], n, result)




if __name__ == '__main__':
    solution = Solution()
    print solution.solve_n_queens(9)
