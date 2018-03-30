# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in
# complexity O(n).
#
# For example,
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
#
# Note:
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
import collections


class Solution(object):
    def min_window(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict = {}
        target = {}
        for c in t:
            if target.get(c) is None:
                target[c] = 1
            else:
                target[c] += 1
        left = 0
        result = ''
        for right in range(len(s)):
            cur = s[right]
            if cur in target:
                if dict.get(cur) is None:
                    dict[cur] = 1
                else:
                    dict[cur] += 1

                if self.bigger(dict, target):
                    while True:
                        key = s[left]
                        if key in target:
                            if dict[key] > target[key]:
                                dict[key] -= 1
                                left += 1
                            else:
                                break
                        else:
                            left += 1

                    candidate = s[left: right + 1]
                    if result == '' or len(candidate) < len(result):
                        result = candidate

        return result

    def bigger(self, d1, d2):
        if len(d1) != len(d2):
            return False

        for key in d1:
            if d1[key] < d2[key]:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()
    s = "aaaaaaaaaaaabbbbbcdd"
    t = 'abcdd'

    # a = collections.Counter(t)
    # print a
    print solution.min_window(s, t)

