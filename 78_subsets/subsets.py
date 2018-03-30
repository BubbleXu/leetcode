# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,3], a solution is:
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for k in range(len(nums) + 1):
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
    print solution.subsets([1, 2, 3])
