# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.

# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]

# Example 2:
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]


class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        self.solve(k, n, [], result)
        return result

    def solve(self, k, n, cur, result):
        if len(cur) == k:
            if sum(cur) == n:
                result.append(cur)
            return

        if sum(cur) >= n:
            return

        for i in range(cur[-1] + 1 if cur else 1, 10):
            self.solve(k, n, cur + [i], result)


if __name__ == '__main__':
    solution = Solution()
    print solution.combinationSum3(3, 9)
