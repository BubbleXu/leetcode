# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
# Each number in C may only be used once in the combination.
#
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]


class Solution(object):
    def combination_sum2(self, candidates, target):
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
            if i > 0 and candidates[i] == candidates[i - 1]:
                continue
            c = candidates[i]
            if c < target:
                self.find(candidates[i + 1:], target - c, cur + [c], result)
            elif c == target:
                cur.append(c)
                result.append(cur)
            else:
                break


if __name__ == '__main__':
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print solution.combination_sum2(candidates, target)
