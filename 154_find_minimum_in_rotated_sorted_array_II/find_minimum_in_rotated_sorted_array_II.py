# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        if left + 1 >= right:
            return min(nums[left], nums[right])

        while left + 1 < right:
            if nums[left] < nums[right]:
                return nums[left]

            middle = (left + right) / 2
            if nums[left] < nums[middle]:
                left = middle
            elif nums[left] > nums[middle]:
                right = middle
            else:
                left += 1
        return min(nums[left], nums[right])