# Description:
#
# Count the number of prime numbers less than a non-negative number, n.


class Solution(object):
    def count_primes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):
            if s[i] == 1:
                s[i * i:n:i] = [0] * len(s[i * i:n:i])
        return sum(s)


if __name__ == '__main__':
    solution = Solution()
    n = 10
    print solution.count_primes(n)
