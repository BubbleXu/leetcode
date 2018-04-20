# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that
#  single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
import collections


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = collections.defaultdict(lambda: 0)
        for x in nums:
            dict[x] += 1
        for x in dict:
            if dict[x] == 1:
                return x