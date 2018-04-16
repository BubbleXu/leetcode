# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


class Solution(object):
    # dp[i][j]: i -> k transaction, j -> day
    # dp[i][j] = max(dp[i][j - 1], prices[j] - prices[m] + dp[i - 1][m]), where m = 0 ... j-1
    # dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff), max_diff = max(max_diff, dp[i - 1][j] - prices[j])
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0

        k = 2
        dp = [[0 for _ in range(len(prices))] for _ in range(k + 1)]
        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print solution.maxProfit([2, 4, 1])
