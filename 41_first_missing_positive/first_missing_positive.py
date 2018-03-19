# Given an unsorted integer array, find the first missing positive integer.
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
# Your algorithm should run in O(n) time and uses constant space.

class Solution(object):
    def first_missing_positive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
        #    so we only have to care about those elements in this range and remove the rest.
        # 2. we can use the array index as the hash to restore the frequency of each number within
        #    the range [1,...,l+1]
        nums.append(0)
        l = len(nums)
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= l:
                nums[i] = 0

        for i in range((len(nums))):
            nums[nums[i] % l] += l

        for i in range(1, (len(nums))):
            if nums[i] / l == 0:
                return i

        return l


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3]
    print solution.first_missing_positive(nums)
