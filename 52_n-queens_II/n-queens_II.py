# Follow up for N-Queens problem.
#
# Now, instead outputting board configurations, return the total number of distinct solutions.


class Solution(object):
    def total_n_queens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.result = 0
        self.solve2([], [], [], n)
        return self.result

    # In this problem, whenever a location (x, y) is occupied,
    # any other locations (p, q) where p + q == x + y or p - q == x - y would be invalid.
    def solve2(self, cur_result, xy_dif, xy_sum, n):
        p = len(cur_result)
        if p == n:
            self.result += 1
            return

        for q in range(n):
            if q not in cur_result and p - q not in xy_dif and p + q not in xy_sum:
                self.solve2(cur_result + [q], xy_dif + [p - q], xy_sum + [p + q], n)


if __name__ == '__main__':
    solution = Solution()
    print solution.total_n_queens(4)