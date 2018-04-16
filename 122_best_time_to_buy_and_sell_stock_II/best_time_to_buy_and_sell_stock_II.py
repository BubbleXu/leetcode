# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit.
# You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times).
# However, you may not engage in multiple transactions at the same time
# (ie, you must sell the stock before you buy again).


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        buy_price, sell_price = prices[0], prices[0]
        result = 0
        for price in prices[1:]:
            if price > sell_price:
                sell_price = price
            elif price < sell_price:
                result += sell_price - buy_price
                buy_price, sell_price = price, price
        result += sell_price - buy_price
        return result