# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: "3+2*2"
# Output: 7
# Example 2:
#
# Input: " 3/2 "
# Output: 1
# Example 3:
#
# Input: " 3+5 / 2 "
# Output: 5

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        num_stack = []
        sign_stack = [('#', 0)]
        priority = {'+': 1, '-': 1, '*': 2, '/': 2}
        tmp_priority = 0
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
                continue

            if s[i] == '(':
                tmp_priority += 1
                i += 1
                continue

            if s[i] == ')':
                tmp_priority -= 1
                i += 1
                continue

            if s[i] in priority:
                while (priority[s[i]] + tmp_priority) <= sign_stack[-1][1]:
                    num2 = num_stack.pop(-1)
                    num1 = num_stack.pop(-1)
                    op = sign_stack.pop(-1)[0]
                    num_stack.append(self.basic_cal(num1, num2, op))
                sign_stack.append((s[i], priority[s[i]] + tmp_priority))
                i += 1
            else:
                j = i + 1
                while j < len(s) and s[j] in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                    j += 1
                num_stack.append(int(s[i:j]))
                i = j

        while sign_stack[-1][0] != '#':
            num2 = num_stack.pop(-1)
            num1 = num_stack.pop(-1)
            op = sign_stack.pop(-1)[0]
            num_stack.append(self.basic_cal(num1, num2, op))
        return num_stack[-1]

    def basic_cal(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        else:
            if num1 * num2 < 0:
                return -(abs(num1) / abs(num2))
            else:
                return num1 / num2


if __name__ == '__main__':
    solution = Solution()
    s = "3/2"
    print solution.calculate(s)