# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution(object):
    def max_product(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result, big, small = nums[0], nums[0], nums[0]
        # for num in nums[1:]:
        #     big, small = max(num, num * big, num * small), min(num, num * big, num * small)
        #     result = max(result, big)
        # return result

        dp_big = [0 for _ in range(len(nums))]
        dp_big[0] = nums[0]
        dp_small = [0 for _ in range(len(nums))]
        dp_small[0] = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            dp_big[i] = max(nums[i], nums[i] * dp_big[i - 1], nums[i] * dp_small[i - 1])
            dp_small[i] = min(nums[i], nums[i] * dp_big[i - 1], nums[i] * dp_small[i - 1])
            result = max(result, dp_big[i])
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [2,-5,-2,-4,3]
    print solution.max_product(nums)
