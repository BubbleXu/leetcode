# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def max_sub_array(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = nums[0]
        max_sum = nums[0]
        for x in nums[1:]:
            cur_sum = max(x, cur_sum + x)
            max_sum = max(cur_sum, max_sum)
        return max_sum


if __name__ == '__main__':
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print solution.max_sub_array(nums)
