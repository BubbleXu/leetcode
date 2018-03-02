# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


class Solution(object):
    def is_valid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 > 0:
            return False

        left_symbol = {
            '(': 0,
            '[': 1,
            '{': 2
        }
        right_symbol = {
            ')': 0,
            ']': 1,
            '}': 2
        }
        stack = []
        for x in s:
            if x in left_symbol:
                stack.append(x)
            else:
                if len(stack) == 0 or left_symbol.get(stack.pop()) != right_symbol.get(x):
                    return False
        return False if len(stack) > 0 else True


if __name__ == '__main__':
    solution = Solution()
    s = '){'
    print solution.is_valid(s)
