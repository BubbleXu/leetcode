# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count = 0
        # for i in range(1, n + 1):
        #     x = i
        #     while x % 5 == 0:
        #         count += 1
        #         x = x / 5
        #
        # return count

        return 0 if n == 0 else n / 5 + self.trailingZeroes(n / 5)
