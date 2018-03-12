# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        max_int = pow(2, 31) - 1
        min_int = -max_int - 1
        while left <= right:
            middle = (left + right) / 2

            # If nums[middle] and target are "on the same side" of nums[0], we just take nums[middle].
            if (nums[middle] < nums[0]) == (target < nums[0]):
                t = nums[middle]
            else:
                t = min_int if target < nums[0] else max_int

            if t < target:
                left = middle + 1
            elif t > target:
                right = middle - 1
            else:
                return middle
        return -1
        # return self.r_search(nums, target, 0, len(nums) - 1)

    def r_search(self, nums, target, left, right):
        if left > right:
            return -1

        middle = (left + right) / 2
        if nums[middle] == target:
            return middle

        if nums[middle] > target:
            if nums[left] < nums[middle]:
                if nums[left] < target:
                    return self.binary_search(nums, target, left, middle - 1)
                elif nums[left] > target:
                    return self.r_search(nums, target, middle + 1, right)
                else:
                    return left
            elif nums[left] > nums[middle]:
                return self.r_search(nums, target, left, middle - 1)
            else:
                return self.r_search(nums, target, middle + 1, right)
        else:
            if nums[middle] < nums[right]:
                if nums[right] > target:
                    return self.binary_search(nums, target, middle + 1, right)
                elif nums[right] < target:
                    return self.r_search(nums, target, left, middle - 1)
                else:
                    return right
            elif nums[middle] > nums[right]:
                return self.r_search(nums, target, middle + 1, right)
            else:
                return self.r_search(nums, target, left, middle - 1)

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
    nums = [3, 1]
    target = 1
    print solution.search(nums, target)
