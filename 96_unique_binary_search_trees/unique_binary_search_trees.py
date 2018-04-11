# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
#
# For example,
# Given n = 3, there are a total of 5 unique BST's.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution(object):
    def num_trees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]

        # return self.imitate(1, n)

        # Catalan Number  (2n)!/((n+1)!*n!)
        # return math.factorial(2 * n) / (math.factorial(n) * math.factorial(n + 1))

    def imitate(self, start, end):
        if start > end:
            return 1

        roots_num = 0
        for i in range(start, end + 1):
            left_roots_num = self.imitate(start, i - 1)
            right_roots_num = self.imitate(i + 1, end)
            roots_num += left_roots_num * right_roots_num
        return roots_num


if __name__ == '__main__':
    solution = Solution()
    print solution.num_trees(4)
