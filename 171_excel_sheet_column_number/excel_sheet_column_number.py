# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {chr(ord('A') + i): i + 1 for i in range(26)}
        result = 0
        power26 = 1
        for x in reversed(s):
            result += dict[x] * power26
            power26 *= 26
        return result