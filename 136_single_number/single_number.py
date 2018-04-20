# Given an array of integers, every element appears twice except for one. Find that single one.
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
import collections


class Solution(object):
    def single_number(self, nums):
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


if __name__ == '__main__':
    solution = Solution()
    print solution.single_number([1,1,2,2,3,4,4])