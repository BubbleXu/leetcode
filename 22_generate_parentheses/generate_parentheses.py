# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution(object):
    def generate_parenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        self.generate(n, n, '', result)
        return result

    def generate(self, n_left, n_right, s, result):
        if n_left == 0 and n_right == 0:
            result.append(s)
            return

        if n_left > 0:
            self.generate(n_left - 1, n_right, s + '(', result)

        if n_left < n_right:
            self.generate(n_left, n_right - 1, s + ')', result)




if __name__ == '__main__':
    solution = Solution()
    print solution.generate_parenthesis(3)