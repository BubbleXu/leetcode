# Compare two version numbers version1 and version2.
# If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
#
# You may assume that the version strings are non-empty and contain only digits and the . character. The . character
# does not represent a decimal point and is used to separate number sequences. For instance, 2.5 is not "two and a
# half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
#
# Here is an example of version numbers ordering:
#
# 0.1 < 1.1 < 1.2 < 13.37

class Solution(object):
    def compare_version(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = map(int, version1.split('.'))
        v2 = map(int, version2.split('.'))
        if len(v1) < len(v2):
            v1 += [0 for _ in range(len(v2) - len(v1))]
        elif len(v1) > len(v2):
            v2 += [0 for _ in range(len(v1) - len(v2))]

        for i in range(min(len(v1), len(v2))):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0


if __name__ == '__main__':
    solution = Solution()
    print solution.compare_version('1.0', '1')