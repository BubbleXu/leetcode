# Given a string s, find the longest palindromic substring in s.
# You may assume that the maximum length of s is 1000.
#
# Example:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
# Example:
#
# Input: "cbbd"
# Output: "bb"


class Solution(object):
    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ''
        l = len(s)
        for center in range(l):
            left = center
            right = center
            while left >= 0 and right < l and s[left] == s[right]:
                if right - left + 1 > len(result):
                    result = s[left: right + 1]
                left -= 1
                right += 1

            if center + 1 < l and s[center] == s[center + 1]:
                left = center
                right = center + 1
                while left >= 0 and right < l and s[left] == s[right]:
                    if right - left + 1 > len(result):
                        result = s[left: right + 1]
                    left -= 1
                    right += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'cbbd'
    print solution.longest_palindrome(s)
