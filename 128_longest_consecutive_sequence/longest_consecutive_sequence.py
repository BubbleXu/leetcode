# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.


class Solution(object):
    def longest_consecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        nums.sort()
        max_length = 1
        cur_length = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                cur_length += 1
            elif nums[i] == nums[i - 1]:
                continue
            else:
                max_length = max(max_length, cur_length)
                cur_length = 1
        return max(max_length, cur_length)

    def longest_consecutive2(self, nums):
        nums_set = set(nums)
        max_length = 0
        for num in nums_set:
            if num - 1 in nums_set:
                continue

            cur_length = 1
            while num + 1 in nums_set:
                num += 1
                cur_length += 1
            max_length = max(max_length, cur_length)
        return max_length


if __name__ == '__main__':
    solution = Solution()
    print solution.longest_consecutive2([1,2,0,1])
