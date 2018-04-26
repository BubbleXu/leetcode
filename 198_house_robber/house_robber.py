# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
# stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount
# of money you can rob tonight without alerting the police.


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) <= 2:
            return max(nums)

        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [2,1,1,2]
    print solution.rob(nums)
