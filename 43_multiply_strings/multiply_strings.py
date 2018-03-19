# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'

        result = ''
        for i in range(len(num1) - 1, -1, -1):
            tmp_result = self.mul_single(num1[i], num2)
            for j in range(len(num1) - 1 - i):
                tmp_result += '0'
            result = self.add_two(result, tmp_result)

        return result

    def mul_single(self, single_num, long_num):
        result = ''
        single_int = int(single_num)
        flag = 0
        for i in range(len(long_num) - 1, -1, -1):
            tmp_result = single_int * int(long_num[i]) + flag
            flag, tmp_result = divmod(tmp_result, 10)
            result = str(tmp_result) + result
        if flag != 0:
            result = str(flag) + result
        return result

    def add_two(self, n1, n2):
        if len(n1) < len(n2):
            short_num, long_num = n1, n2
        else:
            short_num, long_num = n2, n1

        result = ''
        flag = 0
        short_num = short_num[::-1]
        long_num = long_num[::-1]
        for i in range(len(short_num)):
            tmp_result = int(short_num[i]) + int(long_num[i]) + flag
            flag, tmp_result = divmod(tmp_result, 10)
            result += str(tmp_result)

        for i in range(len(short_num), len(long_num)):
            tmp_result = int(long_num[i]) + flag
            flag, tmp_result = divmod(tmp_result, 10)
            result += str(tmp_result)

        if flag != 0:
            result += str(flag)
        return result[::-1]


if __name__ == '__main__':
    solution = Solution()
    num1 = '9133'
    num2 = '0'
    print solution.multiply(num1, num2)
