# Given an input string, reverse the string word by word.
#
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = reversed(s.strip().split(' '))
        result = ''
        for word in words:
            if not word:
                continue

            result += word if not result else ' ' + word
        return result

        # save multiple spaces
        # return ' '.join(reversed(s.strip().split(' ')))


if __name__ == '__main__':
    solution = Solution()
    s = "   a   b "
    print solution.reverseWords(s)
