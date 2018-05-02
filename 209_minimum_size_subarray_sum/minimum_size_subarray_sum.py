# coding: utf-8
# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
#
# Example:
#
# Input: [2,3,1,2,4,3], s = 7
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        result = len(nums) + 1
        left = 0
        cur_sum = 0
        for right in xrange(len(nums)):
            cur_sum += nums[right]
            while cur_sum >= s:
                result = min(result, right - left + 1)
                cur_sum -= nums[left]
                left += 1
        return 0 if result == len(nums) + 1 else result


if __name__ == '__main__':
    solution = Solution()
    s = 7
    nums = [2,3,1,4,3,1]
    print solution.minSubArrayLen(s, nums)

