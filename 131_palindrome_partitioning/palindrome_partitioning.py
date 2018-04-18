# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        self.solve(s, [], result)
        return result

    def solve(self, s, cur, result):
        if not s:
            result.append(cur)
            return

        for i in range(len(s)):
            if self.is_palindrome(s[:i+1]):
                self.solve(s[i+1:], cur + [s[:i+1]], result)

    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    s = 'fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi'
    print solution.partition(s)
