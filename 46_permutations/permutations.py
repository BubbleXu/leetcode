# Given a collection of distinct numbers, return all possible permutations.
#
# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        cur = []
        self.do_permute(nums, cur, result)
        return result

    def do_permute(self, nums, cur, result):
        if len(nums) == 0:
            result.append(cur)
            return

        for i in range(len(nums)):
            next_nums = nums[:]
            candidate = next_nums.pop(i)
            self.do_permute(next_nums, cur + [candidate], result)


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    print solution.permute(nums)
