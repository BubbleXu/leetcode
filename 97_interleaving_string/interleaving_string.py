# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
#
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.

class Solution(object):
    def is_interleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        if n + m != len(s3):
            return False

        dp = [[False for j in range(m + 1)] for i in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, m + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[j - 1 + i]) or \
                           (dp[i - 1][j] and s1[i - 1] == s3[i - 1 + j])

        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print solution.is_interleave(s1, s2, s3)
