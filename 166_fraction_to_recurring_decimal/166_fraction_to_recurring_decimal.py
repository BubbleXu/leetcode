# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".


class Solution(object):
    def fraction_to_decimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        quotient, remainder = divmod(numerator, denominator)
        if remainder == 0:
            return str(quotient)

        result = ''
        if quotient < 0:
            result += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        quotient, remainder = divmod(numerator, denominator)

        result += str(quotient)
        result += '.'
        numerator = remainder
        i = len(result)
        dict = {}
        while numerator != 0:
            if not dict.get(numerator):
                dict[numerator] = i
            else:
                i = dict[numerator]
                result = result[:i] + '(' + result[i:] + ')'
                return result
            numerator *= 10
            quotient, remainder = divmod(numerator, denominator)
            result += str(quotient)
            numerator = remainder
            i += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.fraction_to_decimal(-50, 8)
