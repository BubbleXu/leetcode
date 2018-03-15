# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# The same repeated number may be chosen from C unlimited number of times.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7,
# A solution set is:
# [
#   [7],
#   [2, 2, 3]
# ]


class Solution(object):
    def combination_sum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        cur = []
        result = []
        self.find(candidates, target, cur, result)
        return result

    def find(self, candidates, target, cur, result):
        for i in range(len(candidates)):
            c = candidates[i]
            if c < target:
                self.find(candidates[i:], target - c, cur + [c], result)
            elif c == target:
                cur.append(c)
                result.append(cur)
            else:
                break


if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print solution.combination_sum(candidates, target)
