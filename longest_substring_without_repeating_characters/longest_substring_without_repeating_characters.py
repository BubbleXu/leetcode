# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3.
# Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution(object):
    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        begin, end = 0, 0
        result = 0
        for end in range(len(s)):
            if dict.get(s[end]) is not None:
                begin = max(dict.get(s[end]), begin)

            result = max(result, end - begin + 1)
            dict[s[end]] = end + 1

        return result


if __name__ == '__main__':
    solution = Solution()
    test_set = ["abcabcbb", "bbbbb", "pwwkew"]
    for s in test_set:
        print solution.length_of_longest_substring(s)

