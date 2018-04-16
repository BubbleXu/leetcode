# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.
#
# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.
# For the purpose of this problem, we define empty string as valid palindrome.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1
        dict = {str(x) for x in range(10)}
        for i in range(26):
            dict.add(chr(i + ord('a')))
            dict.add(chr(i + ord('A')))
        while left < right:
            while left < len(s) and s[left] not in dict:
                left += 1
            while right >= 0 and s[right] not in dict:
                right -= 1
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    s = ".,"
    print solution.isPalindrome(s)
