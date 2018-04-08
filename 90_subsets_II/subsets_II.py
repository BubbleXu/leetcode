# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets_with_dup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
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
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.solve(nums[i + 1:], left - 1, cur + [nums[i]], result)


if __name__ == '__main__':
    solution = Solution()
    print solution.subsets_with_dup([4,4,4,1,4])