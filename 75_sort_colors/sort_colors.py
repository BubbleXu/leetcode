# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
# with the colors in the order red, white and blue.
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# Note:
# You are not suppose to use the library's sort function for this problem.


class Solution(object):
    def sort_colors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        self.quick_sort(nums, 0, len(nums) - 1)

    def quick_sort(self, nums, left, right):
        if left >= right:
            return

        pivot = nums[left]
        i = left
        j = right
        while i < j:
            while nums[i] <= pivot and i < right:
                i += 1
            while nums[j] >= pivot and j > left:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]

        nums[left], nums[j] = nums[j], nums[left]
        self.quick_sort(nums, left, j - 1)
        self.quick_sort(nums, j + 1, right)


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 2, 1]
    solution.sort_colors(nums)
    print nums
