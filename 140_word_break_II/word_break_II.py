# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to
# construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain
# duplicate words.
#
# Return all such possible sentences.
#
# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].
#
# A solution is ["cats and dog", "cat sand dog"].


class Solution(object):
    def word_break(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        return self.solve(s, wordDict, {})

    # memory: s -> ["X1 X2", "X3 X4 X5"]
    def solve(self, s, word_dict, memory):
        if s in memory:
            return memory[s]

        if not s:
            return []

        result = []
        for word in word_dict:
            if not s.startswith(word):
                continue

            if len(s) == len(word):
                result.append(word)
            else:
                rest = self.solve(s[len(word):], word_dict, memory)
                for item in rest:
                    result.append(word + ' ' + item)
        memory[s] = result
        return result



if __name__ == '__main__':
    solution = Solution()
    s = "aaaaaaa"
    wordDict = ["aaaa","aa","a"]
    print solution.word_break(s, wordDict)
