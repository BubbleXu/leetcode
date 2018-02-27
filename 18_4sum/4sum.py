# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
#
# Note: The solution set must not contain duplicate quadruplets.
#
# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]


class Solution(object):
    def four_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) <= 3:
            return result

        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            cur_number = nums[i]
            three_sum_result = self.three_sum(nums[i+1:], target - cur_number)
            for combination in three_sum_result:
                result.append([cur_number] + combination)
        return result

    def three_sum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) <= 2:
            return result

        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                sum = nums[left] + nums[middle] + nums[right]
                if sum > target:
                    right -= 1
                elif sum < target:
                    middle += 1
                else:
                    result.append([nums[left], nums[middle], nums[right]])
                    while middle < right and nums[middle] == nums[middle + 1]:
                        middle += 1
                    while middle < right and nums[right] == nums[right - 1]:
                        right -= 1
                    middle += 1
                    right -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,-2,-5,-4,-3,3,3,5]
    print solution.four_sum(nums, -11)

