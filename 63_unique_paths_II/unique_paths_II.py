# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.


class Solution(object):
    def unique_paths_with_obstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(1, m):
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, n):
            obstacleGrid[0][j] = obstacleGrid[0][j - 1] if obstacleGrid[0][j] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1] if obstacleGrid[i][j] == 0 else 0

        return obstacleGrid[m - 1][n - 1]


if __name__ == '__main__':
    solution = Solution()
    obstacleGrid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print solution.unique_paths_with_obstacles(obstacleGrid)
