# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
#
# For example:
# Given array A = [2,3,1,1,4]
#
# The minimum number of jumps to reach the last index is 2.
# (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
#
# Note:
# You can assume that you can always reach the last index.


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.min_count_jumps = len(nums)
        self.do_jump(nums, 0, 0)
        return self.min_count_jumps

    def do_jump(self, nums, cur_index, cur_count_jumps):
        if cur_index == len(nums) - 1:
            self.min_count_jumps = min(self.min_count_jumps, cur_count_jumps)
            return

        if cur_count_jumps >= self.min_count_jumps:
            return

        max_step = nums[cur_index]
        for step in range(1, max_step + 1):
            if cur_index + step < len(nums):
                self.do_jump(nums, cur_index + step, cur_count_jumps + 1)

    def jump2(self, nums):
        queue = [(0, 0)]
        while True:
            cur_index, cur_count_jumps = queue.pop(0)

            for step in reversed(range(0, nums[cur_index] + 1)):
                if cur_index + step >= len(nums) - 1:
                    return cur_count_jumps + 1 if step > 0 else cur_count_jumps
                else:
                    queue.append((cur_index + step, cur_count_jumps + 1))

    def jump3(self, nums):
        jumps = 0
        current_jump_max = 0
        previous_jump_max = 0

        for i in range(len(nums) - 1):
            current_jump_max = max(current_jump_max, i + nums[i])
            if i == previous_jump_max:
                jumps += 1
                previous_jump_max = current_jump_max
        return jumps


if __name__ == '__main__':
    solution = Solution()
    nums = [9,4,5,4,1,8,1,2,0,7,8,7,0,6,6,1,1,2,5,0,9,8,4,7,9,6,8,1,4,0,8,5,5,3,9,8,1,2,2,3,0,1,3,2,7,9,3,0,1]
    # nums = [0]
    print solution.jump2(nums)
