# Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
#
# You may assume the integer do not contain any leading zero, except the number 0 itself.
#
# The digits are stored such that the most significant digit is at the head of the list.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = []
        flag = 1
        for num in reversed(digits):
            cur = num + flag
            if cur >= 10:
                cur -= 10
                flag = 1
            else:
                flag = 0
            result.append(cur)

        if flag == 1:
            result.append(1)
        result.reverse()
        return result
