# Write an algorithm to determine if a number is "happy".
#
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
#
# Example: 19 is a happy number
#
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution(object):
    def is_happy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        memory = set()
        cur = n
        while cur != 1:
            next = 0
            for x in str(cur):
                next += int(x) ** 2

            if next in memory:
                return False

            memory.add(next)
            cur = next
        return True


if __name__ == '__main__':
    solution = Solution()
    print solution.is_happy(21)