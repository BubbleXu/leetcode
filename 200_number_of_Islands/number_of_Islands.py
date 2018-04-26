# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water
# and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid
# are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m <= 0:
            return 0

        n = len(grid[0])
        if n <= 0:
            return 0

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    result += 1
                    grid[i][j] = '*'
                    queue = [(i, j)]
                    while queue:
                        x, y = queue.pop(0)
                        # up
                        if x - 1 >= 0 and grid[x - 1][y] == '1':
                            grid[x - 1][y] = '*'
                            queue.append((x - 1, y))

                        # right
                        if y + 1 < n and grid[x][y + 1] == '1':
                            grid[x][y + 1] = '*'
                            queue.append((x, y + 1))

                        # down
                        if x + 1 < m and grid[x + 1][y] == '1':
                            grid[x + 1][y] = '*'
                            queue.append((x + 1, y))

                        # left
                        if y - 1 >= 0 and grid[x][y - 1] == '1':
                            grid[x][y - 1] = '*'
                            queue.append((x, y - 1))

        return result


if __name__ == '__main__':
    solution = Solution()
    grid = [
         ["1", "0", "0", "1", "1", "1", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "0", "1", "0"],
         ["0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "0", "0", "1", "0", "1", "0"],
         ["0", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "1", "1", "0", "0", "1", "0", "0", "1"],
         ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
         ["1", "0", "0", "0", "0", "1", "0", "1", "0", "1", "1", "0", "0", "0", "0", "0", "0", "1", "0", "1"],
         ["0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1"],
         ["0", "0", "0", "1", "0", "1", "0", "0", "1", "1", "0", "1", "0", "1", "1", "0", "1", "1", "1", "0"],
         ["0", "0", "0", "0", "1", "0", "0", "1", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1"],
         ["0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0"],
         ["1", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "1", "0", "1", "0"],
         ["0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "1", "0", "1", "1", "1", "0", "1", "1", "0", "0"],
         ["1", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1"],
         ["0", "1", "0", "0", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "1", "0", "0", "0"],
         ["0", "0", "1", "1", "1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0"],
         ["1", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "1"],
         ["1", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0"],
         ["0", "1", "1", "0", "0", "0", "1", "1", "1", "0", "1", "0", "1", "0", "1", "1", "1", "1", "0", "0"],
         ["0", "1", "0", "0", "0", "0", "1", "1", "0", "0", "1", "0", "1", "0", "0", "1", "0", "0", "1", "1"],
         ["0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "0", "0", "1", "1", "0", "0", "0"]
    ]
    print solution.numIslands(grid)