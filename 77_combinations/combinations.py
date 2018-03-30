# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# For example,
# If n = 4 and k = 2, a solution is:
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        nums = [i for i in range(1, n + 1)]
        self.solve(nums, k, [], result)
        return result

    def solve(self, nums, left, cur, result):
        if len(nums) < left:
            return

        if left == 0:
            result.append(cur)
            return

        for i in range(len(nums)):
            self.solve(nums[i + 1:], left - 1, cur + [nums[i]], result)


if __name__ == '__main__':
    solution = Solution()
    print solution.combine(4, 2)