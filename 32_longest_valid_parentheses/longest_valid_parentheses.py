# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.


class Solution(object):
    def longest_valid_parentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0

        n_left = 0
        n_right = 0
        result = 0
        for i in range(len(s)):
            if s[i] == '(':
                n_left += 1
            else:
                n_right += 1

            if n_left == n_right:
                result = max(result, n_left * 2)
            elif n_left < n_right:
                n_left = 0
                n_right = 0

        n_left = 0
        n_right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                n_left += 1
            else:
                n_right += 1

            if n_left == n_right:
                result = max(result, n_left * 2)
            elif n_left > n_right:
                n_left = 0
                n_right = 0

        return result


if __name__ == '__main__':
    solution = Solution()
    s = ")()())"
    print solution.longest_valid_parentheses(s)
