# Divide two integers without using multiplication, division and mod operator.
#
# If it is overflow, return MAX_INT.


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return 0

        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign

        result = 0
        while dividend >= divisor:
            count = 1
            new_divisor = divisor
            while new_divisor + new_divisor < dividend:
                count += count
                new_divisor += new_divisor
            dividend -= new_divisor
            result += count

        if sign == -1:
            result = -result
        return min(max(-2147483648, result), 2147483647)


if __name__ == '__main__':
    solution = Solution()
    print solution.divide(-2147483648, -1)
