# coding: utf-8
# Implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") → false
# isMatch("aa","aa") → true
# isMatch("aaa","aa") → false
# isMatch("aa", "*") → true
# isMatch("aa", "a*") → true
# isMatch("ab", "?*") → true
# isMatch("aab", "c*a*b") → false


class Solution(object):
    def is_match(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            return s == ''

        if s == '':
            return len(p) == p.count('*')

        first_match = p[0] in [s[0], '?']
        if first_match:
            return self.is_match(s[1:], p[1:])
        elif p[0] == '*':
            return self.is_match(s[1:], p) or self.is_match(s, p[1:])
        else:
            return False

    def is_match2(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False

        dp = [True] + [False] * length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n + 1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length + 1):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    s = "bbbbbbbbaaabbaabbabaaaaaabbbababbbaaabbaabbbababbaaaa"
    p = "**a*bbaabb**bbab*a**"
    print solution.is_match(s, p)
