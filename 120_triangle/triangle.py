# Given a triangle,
# find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space,
# where n is the total number of rows in the triangle.
import copy


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        result = copy.deepcopy(triangle)
        for i in range(1, len(triangle)):
            for j in range(i + 1):
                if j == 0:
                    result[i][j] = result[i - 1][j] + triangle[i][j]
                elif j == i:
                    result[i][j] = result[i - 1][j - 1] + triangle[i][j]
                else:
                    result[i][j] = min(result[i - 1][j - 1], result[i - 1][j]) + triangle[i][j]

        return min(result[-1])
