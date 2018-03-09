# coding: utf-8

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible,
# it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# The replacement must be in-place, do not allocate extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def next_permutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return

        for i in range(len(nums) - 2, -1, -1):
            j = i + 1
            if nums[i] < nums[j]:
                for k in range(len(nums) - 1, j - 1, -1):
                    if nums[k] > nums[i]:
                        nums[i], nums[k] = nums[k], nums[i]
                        tmp = nums[j:]
                        tmp.reverse()
                        nums[j:] = tmp
                        return

        nums.reverse()


if __name__ == '__main__':
    solution = Solution()
    nums = [3,7,6,2,5,4,3,1]
    solution.next_permutation(nums)
    print nums
