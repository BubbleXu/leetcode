# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# For example:
# A = [2,3,1,1,4], return true.
#
# A = [3,2,1,0,4], return false.


class Solution(object):
    def can_jump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_pos = len(nums) - 1
        for i in reversed(range(len(nums))):
            if last_pos <= i + nums[i]:
                last_pos = i
        return last_pos == 0

    def can_jump2(self, nums):
        current_jump_max = 0
        for i in range(len(nums) - 1):
            current_jump_max = max(current_jump_max, i + nums[i])
            if i == current_jump_max:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,1,0,4]
    print solution.can_jump(nums)
