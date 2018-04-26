# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        if k >= len(prices) / 2:
            return self.quick_solve(prices)

        dp = [[0 for _ in range(len(prices))] for _ in range(k + 1)]
        for i in range(1, k + 1):
            max_diff = -prices[0]
            for j in range(1, len(prices)):
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        return dp[-1][-1]

    # when k >= len(prices) / 2, greedy solution
    def quick_solve(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            gap = prices[i] - prices[i - 1]
            if gap > 0:
                profit += gap
        return profit
