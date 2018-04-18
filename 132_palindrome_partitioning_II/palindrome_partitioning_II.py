# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.


class Solution(object):
    def min_cut(self, s):
        """
        :type s: str
        :rtype: int
        """
        queue = [s]
        result = 0
        while queue:
            next_queue = []
            while queue:
                cur = queue.pop()
                if self.is_palindrome(cur):
                    return result

                for i in range(1, len(cur)):
                    if self.is_palindrome(cur[:i]):
                        next_queue.append(cur[i:])
            result += 1
            queue = next_queue

    def is_palindrome(self, s):
        return s == s[::-1]

    def min_cut2(self, s):
        # number of cuts for the first k characters
        cut = range(-1, len(s))
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                if s[i:j] == s[j:i:-1]:
                    cut[j + 1] = min(cut[j + 1], cut[i] + 1)
        return cut[-1]

    def min_cut3(self, s):
        # acceleration
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        cut = range(-1, len(s))
        for i in range(len(s)):
            r1, r2 = 0, 0
            # use i as origin, and gradually enlarge radius if a palindrome exists
            # odd palindrome
            while i - r1 >= 0 and i + r1 < len(s) and s[i - r1] == s[i + r1]:
                cut[i + r1 + 1] = min(cut[i + r1 + 1], cut[i - r1] + 1)
                r1 += 1
            # even palindrome
            while i - r2 >= 0 and i + r2 + 1 < len(s) and s[i - r2] == s[i + r2 + 1]:
                cut[i + r2 + 2] = min(cut[i + r2 + 2], cut[i - r2] + 1)
                r2 += 1
        return cut[-1]


if __name__ == '__main__':
    solution = Solution()
    s = 'fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi'
    print solution.min_cut3(s)
