# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].


class Solution(object):
    def search_range(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        cur = self.binary_search(nums, target, left, right)
        if cur == -1:
            return [-1, -1]
        else:
            begin = cur
            tmp_begin = begin
            while True:
                tmp_begin = self.binary_search(nums, target, left, tmp_begin - 1)
                if tmp_begin != -1:
                    begin = tmp_begin
                else:
                    break

            end = cur
            tmp_end = end
            while True:
                tmp_end = self.binary_search(nums, target, tmp_end + 1, right)
                if tmp_end != -1:
                    end = tmp_end
                else:
                    break
        return [begin, end]

    def binary_search(self, nums, target, left, right):
        if left > right:
            return -1

        middle = (left + right) / 2
        if nums[middle] == target:
            return middle

        if nums[middle] > target:
            return self.binary_search(nums, target, left, middle - 1)
        else:
            return self.binary_search(nums, target, middle + 1, right)


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 3
    print solution.search_range(nums, target)

