# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.


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
            else:
                right = middle
        return min(nums[left], nums[right])
