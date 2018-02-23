# Determine whether an integer is a palindrome. Do this without extra space.


class Solution(object):
    def is_palindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # -1 and 10 is not palindrome
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverse_x = 0
        while x > reverse_x:
            reverse_x = reverse_x * 10 + x % 10
            x /= 10

        return x == reverse_x or x == reverse_x / 10


if __name__ == '__main__':
    solution = Solution()
    x = 101
    print solution.is_palindrome(x)