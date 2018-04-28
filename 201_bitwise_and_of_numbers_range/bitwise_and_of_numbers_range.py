# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#
# For example, given the range [5, 7], you should return 4.

class Solution(object):
    def range_bitwise_and(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # the bitwise and of the range
        # is keeping the common bits of m and n from left to right until the first bit that they are different,
        # padding zeros for the rest.
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i


if __name__ == '__main__':
    solution = Solution()
    m = 5
    n = 7
    print solution.range_bitwise_and(m, n)
