# Write a function to find the longest common prefix string amongst an array of strings.


class Solution(object):
    def longest_common_prefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <= 0:
            return ''

        result = strs[0]
        for i in range(1, len(strs)):
            result = self.find_longest_common_prefix_among_two(result, strs[i])
        return result

    def find_longest_common_prefix_among_two(self, s1, s2):
        result = ''
        limit = len(s1) if len(s1) < len(s2) else len(s2)
        for i in range(limit):
            if s1[i] == s2[i]:
                result += s1[i]
            else:
                break
        return result


if __name__ == '__main__':
    solution = Solution()
    strs = ['a', 'b']
    print solution.longest_common_prefix(strs)
