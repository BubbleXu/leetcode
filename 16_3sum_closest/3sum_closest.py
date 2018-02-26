# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
# Return the sum of the three integers. You may assume that each input would have exactly one solution.

# For example, given array S = {-1 2 1 -4}, and target = 1.
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution(object):
    def three_sum_closest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        if len(nums) <= 2:
            return result

        nums.sort()
        min_gap = 999999999
        for left in range(len(nums) - 2):
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                sum = nums[left] + nums[middle] + nums[right]
                gap = abs(sum - target)
                if gap < min_gap:
                    min_gap = gap
                    result = sum

                if sum > target:
                    right -= 1
                elif sum < target:
                    middle += 1
                else:
                    return sum
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 2, 1, -4]
    print solution.three_sum_closest(nums, 1)

