# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
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
        count = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
                count = 0
            else:
                if count == 0:
                    i += 1
                    nums[i] = nums[j]
                    count += 1

        return i + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,2,2,3]
    print solution.remove_duplicates(nums)
    print nums