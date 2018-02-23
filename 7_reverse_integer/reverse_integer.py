# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output:  321

# Example 2:
# Input: -123
# Output: -321


# Example 3:
# Input: 120
# Output: 21


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        sign = 1
        if x < 0:
            x = -x
            sign = -1

        while x != 0:
            x, val = divmod(x, 10)
            if result > 214748364 or (result == 214748364 and x > 7):
                return 0
            result = result * 10 + val
        return sign * result


if __name__ == '__main__':
    solution = Solution()
    x = 1021
    print solution.reverse(x)
