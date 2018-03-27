# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?
#
#
# Above is a 3 x 7 grid. How many possible unique paths are there?
#
# Note: m and n will be at most 100.


class Solution(object):
    def unique_paths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for j in range(n)] for i in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[m - 1][n - 1]
        # self.count = 0
        # self.solve(0, 0, m, n)
        # return self.count

    def solve(self, x, y, m, n):
        if x == m - 1 and y == n - 1:
            self.count += 1
            return

        if x < m - 1:
            self.solve(x + 1, y, m, n)

        if y < n - 1:
            self.solve(x, y + 1, m, n)


if __name__ == '__main__':
    solution = Solution()
    print solution.unique_paths(1, 1)
