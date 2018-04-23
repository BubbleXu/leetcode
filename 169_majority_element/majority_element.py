# coding: utf-8
# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊
# n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = collections.defaultdict(lambda: 0)
        limit = len(nums) / 2
        for x in nums:
            dict[x] += 1
            if dict[x] > limit:
                return x

    # Boyer-Moore Algorithm
    def majority_element(self, nums):
        candidate = 0
        count = 0
        for x in nums:
            if count == 0:
                candidate = x

            if candidate == x:
                count += 1
            else:
                count -= 1
        return candidate

