# Implement atoi to convert a string to an integer.
#
# Hint: Carefully consider all possible input cases.
# If you want a challenge, please do not see below and ask yourself what are the possible input cases.
#
# Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
# You are responsible to gather all the input requirements up front.


class Solution(object):
    def my_atoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        result = 0
        i = 0
        sign = 1
        n = len(str)

        if n == 0:
            return 0

        while i < n and str[i] == ' ':
            i += 1

        if i < n and (str[i] == '-' or str[i] == '+'):
            sign = 1 - 2 * (str[i] == '-')
            i += 1

        while i < n and ord('0') <= ord(str[i]) <= ord('9'):
            cur = int(str[i])
            if result > 214748364 or (result == 214748364 and cur > 7):
                if sign == 1:
                    return 2147483647
                else:
                    return -2147483648
            result = result * 10 + cur
            i += 1
        return result * sign


if __name__ == '__main__':
    solution = Solution()
    print solution.my_atoi("1234")
