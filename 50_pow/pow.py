# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100


class Solution(object):
    def my_pow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            return 1.0 / self.my_pow(x, -n)

        if n % 2 > 0:
            return x * self.my_pow(x, n - 1)
        else:
            return self.my_pow(x * x, n / 2)


if __name__ == '__main__':
    solution = Solution()
    print solution.my_pow(1.00001, 123456)
