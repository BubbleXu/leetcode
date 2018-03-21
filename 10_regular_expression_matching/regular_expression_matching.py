# coding: utf-8
# Implement regular expression matching with support for '.' and '*'.

# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
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
# isMatch("aa", "a*") → true
# isMatch("aa", ".*") → true
# isMatch("ab", ".*") → true
# isMatch("aab", "c*a*b") → true


class Solution(object):
    def is_match(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            return s == ''

        first_match = (s != '') and p[0] in [s[0], '.']
        if len(p) > 1 and p[1] == '*':
            return self.is_match(s, p[2:]) or (first_match and self.is_match(s[1:], p))
        else:
            return first_match and self.is_match(s[1:], p[1:])


if __name__ == '__main__':
    solution = Solution()
    print solution.is_match('aab', 'c*a*b')
