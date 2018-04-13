# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j]
                if s[i - 1] == t[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]

        return dp[-1][-1]
        # return self.solve(s, t, 0)

    def solve(self, s, t, cur_position):
        if len(s) < len(t):
            return 0

        if len(s) == len(t):
            if s == t:
                return 1
            else:
                return 0

        result = 0
        for i in range(cur_position, len(s)):
            result += self.solve(s[:i] + s[i+1:], t, i)
        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'aabb'
    t = 'abb'
    print solution.numDistinct(s, t)
