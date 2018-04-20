# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be
# segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not
# contain duplicate words.
#
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
#
# Return true because "leetcode" can be segmented as "leet code".


class Solution(object):
    def word_break(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[-1]


        # self.result = False
        # word_set = set(wordDict)
        # self.solve(s, word_set)
        # return self.result

    def solve(self, s, word_set):
        if not s:
            self.result = True
            return

        for word in word_set:
            if s[:len(word)] == word:
                self.solve(s[len(word):], word_set)
            if self.result:
                return


if __name__ == '__main__':
    solution = Solution()
    s = 'leetcode'
    wordDict = ["leet", "code"]
    print solution.word_break(s, wordDict)



