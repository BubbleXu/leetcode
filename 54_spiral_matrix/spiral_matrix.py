# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# For example,
# Given the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution(object):
    def spiral_order(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        m = len(matrix)
        if m == 0:
            return result

        n = len(matrix[0])
        if n == 0:
            return result

        row, col = 0, 0
        direction = 'right'
        occupy = [[0 for j in range(n)] for i in range(m)]
        while True:
            result.append(matrix[row][col])
            occupy[row][col] = 1
            if direction == 'right':
                if col + 1 < n and occupy[row][col + 1] == 0:
                    col += 1
                elif row + 1 < m and occupy[row + 1][col] == 0:
                    row += 1
                    direction = 'down'
                else:
                    break
            elif direction == 'down':
                if row + 1 < m and occupy[row + 1][col] == 0:
                    row += 1
                elif col - 1 >= 0 and occupy[row][col - 1] == 0:
                    col -= 1
                    direction = 'left'
                else:
                    break
            elif direction == 'left':
                if col - 1 >= 0 and occupy[row][col - 1] == 0:
                    col -= 1
                elif row - 1 >= 0 and occupy[row - 1][col] == 0:
                    row -= 1
                    direction = 'up'
                else:
                    break
            elif direction == 'up':
                if row - 1 >= 0 and occupy[row - 1][col] == 0:
                    row -= 1
                elif col + 1 < n and occupy[row][col + 1] == 0:
                    col += 1
                    direction = 'right'
                else:
                    break

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [
        [2, 5, 8],
        [4, 0, -1]
    ]
    print solution.spiral_order(nums)
