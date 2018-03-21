# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# For example,
# [1,1,2] have the following unique permutations:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]


class Solution(object):
    def permute_unique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        cur = []
        nums.sort()
        self.do_permute(nums, cur, result)
        return result

    def do_permute(self, nums, cur, result):
        if len(nums) == 0:
            result.append(cur)
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            next_nums = nums[:]
            candidate = next_nums.pop(i)
            self.do_permute(next_nums, cur + [candidate], result)


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,2]
    print solution.permute_unique(nums)
