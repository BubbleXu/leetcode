# Given two binary strings, return their sum (also a binary string).
#
# For example,
# a = "11"
# b = "1"
# Return "100".


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) > len(b):
            a, b = b, a

        result = ''
        flag = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(len(a)):
            cur = int(a[i]) + int(b[i]) + flag
            if cur >= 2:
                cur -= 2
                flag = 1
            else:
                flag = 0
            result = str(cur) + result

        for i in range(len(a), len(b)):
            cur = int(b[i]) + flag
            if cur >= 2:
                cur -= 2
                flag = 1
            else:
                flag = 0
            result = str(cur) + result

        if flag == 1:
            result = '1' + result
        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.addBinary("1010", "1011")

