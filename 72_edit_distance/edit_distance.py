# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each
# operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
# a) Insert a character
# b) Delete a character
# c) Replace a character


class Solution(object):
    def min_distance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # dp[i][j] stands for word1[0 ... i-1] -> word2[0 ... j-1]
        # dp[i][0] = i;
        # dp[0][j] = j;
        # dp[i][j] = dp[i - 1][j - 1], if word1[i - 1] = word2[j - 1];
        # dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1), otherwise.
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
        # return self.solve(word1, word2)

    def solve(self, word1, word2):
        if word1 == '':
            return len(word2)

        if word2 == '':
            return len(word1)

        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                return 1 + min(self.solve(word1[i:], word2[i + 1:]),
                               self.solve(word1[i + 1:], word2[i:]),
                               self.solve(word1[i + 1:], word2[i + 1:]))

        return max(len(word1), len(word2)) - min(len(word1), len(word2))


if __name__ == '__main__':
    solution = Solution()
    word1 = "dinitrophenylhydrazine"
    word2 = 'acetylphenylhydrazine'
    print solution.min_distance(word1, word2)