# coding: utf-8
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
#
# Input: [3,2,3]
# Output: [3]
# Example 2:
#
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        count1, count2 = 0, 0
        cur1, cur2 = None, None
        for x in nums:
            if x == cur1:
                count1 += 1
            elif x == cur2:
                count2 += 1
            elif count1 == 0:
                cur1 = x
                count1 += 1
            elif count2 == 0:
                cur2 = x
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        return [x for x in (cur1, cur2) if nums.count(x) > len(nums) / 3]


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,3,3,2,2,2]
    print solution.majorityElement(nums)