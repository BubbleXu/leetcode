# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
# Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution(object):
    def three_sum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) <= 2:
            return result

        nums.sort()
        for left in range(len(nums) - 2):
            if nums[left] > 0:
                break
            if left > 0 and nums[left] == nums[left - 1]:
                continue

            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                sum = nums[left] + nums[middle] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
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
    nums = [-1, 0, 1, 2, -1, -4]
    print solution.three_sum(nums)

