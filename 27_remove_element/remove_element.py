# Given an array and a value, remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# Example:
#
# Given nums = [3,2,2,3], val = 3,
# Your function should return length = 2, with the first two elements of nums being 2.


class Solution(object):
    def remove_element(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = -1
        for j in range(0, len(nums)):
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [3,2,2,3]
    print solution.remove_element(nums, 3)
    print nums
