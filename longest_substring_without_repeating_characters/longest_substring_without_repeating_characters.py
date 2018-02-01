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
        for i in range(len(s)):
            if dict.get(s[i]) is not None:
                result = max(result, end - begin)
                while begin <= dict.get(s[i]):
                    dict.pop(s[begin])
                    begin += 1
            dict[s[i]] = i
            end += 1
        return max(result, end - begin)


if __name__ == '__main__':
    solution = Solution()
    test_set = ["abcabcbb", "bbbbb", "pwwkew"]
    for s in test_set:
        print solution.length_of_longest_substring(s)

