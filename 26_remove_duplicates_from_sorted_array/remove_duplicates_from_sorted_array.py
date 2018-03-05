# Given a sorted array,
# remove the duplicates in-place such that each element appear only once and return the new length.
#
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
#
# Example:
#
# Given nums = [1,1,2],
# Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
# It doesn't matter what you leave beyond the new length.


class Solution(object):
    def remove_duplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1]
    print solution.remove_duplicates(nums)
    print nums
