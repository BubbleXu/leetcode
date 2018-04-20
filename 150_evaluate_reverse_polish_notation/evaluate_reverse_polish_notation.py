# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        priority = {'+': 1, '-': 1, '*': 2, '/': 2}
        num_stack = []
        for x in tokens:
            if not priority.get(x):
                num_stack.append(int(x))
                continue

            num2 = num_stack.pop(-1)
            num1 = num_stack.pop(-1)
            num_stack.append(self.calculate(num1, num2, x))
        return num_stack[-1]

    def calculate(self, n1, n2, operator):
        if operator == '+':
            return n1 + n2
        elif operator == '-':
            return n1 - n2
        elif operator == '*':
            return n1 * n2
        else:
            if n1 * n2 < 0:
                return -(abs(n1) / abs(n2))
            else:
                return n1 / n2


if __name__ == '__main__':
    solution = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print solution.evalRPN(tokens)
