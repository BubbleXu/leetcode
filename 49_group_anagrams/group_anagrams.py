# Given an array of strings, group anagrams together.
#
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
#
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note: All inputs will be in lower-case.


class Solution(object):
    def group_anagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for word in strs:
            chars = []
            for c in word:
                chars.append(c)
            chars.sort()
            key = ''.join(chars)
            if dict.get(key) is None:
                dict[key] = [word]
            else:
                dict[key].append(word)

        result = []
        for key in dict:
            result.append(dict[key])
        return result


if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print solution.group_anagrams(strs)
