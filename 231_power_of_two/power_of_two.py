# encoding: utf-8
# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
#
# Input: 1
# Output: true
# Example 2:
#
# Input: 16
# Output: true
# Example 3:
#
# Input: 218
# Output: false

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # For example, 8 = 1000b and 8 − 1 = 7 = 0111b.
        # If x and x − 1 are binary ANDed then the result is only 0 if x is a power of two

        return n > 0 and not (n & n-1)

        # if n == 1:
        #     return True
        #
        # if n % 2 != 0 or n == 0:
        #     return False
        #
        # return self.isPowerOfTwo(n / 2)
