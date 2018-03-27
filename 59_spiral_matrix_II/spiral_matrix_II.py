# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generate_matrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        if n == 0:
            return result

        row, col = 0, 0
        direction = 'right'
        result = [[0 for j in range(n)] for i in range(n)]
        num = 1
        while True:
            result[row][col] = num
            num += 1

            if direction == 'right':
                if col + 1 < n and result[row][col + 1] == 0:
                    col += 1
                elif row + 1 < n and result[row + 1][col] == 0:
                    row += 1
                    direction = 'down'
                else:
                    break
            elif direction == 'down':
                if row + 1 < n and result[row + 1][col] == 0:
                    row += 1
                elif col - 1 >= 0 and result[row][col - 1] == 0:
                    col -= 1
                    direction = 'left'
                else:
                    break
            elif direction == 'left':
                if col - 1 >= 0 and result[row][col - 1] == 0:
                    col -= 1
                elif row - 1 >= 0 and result[row - 1][col] == 0:
                    row -= 1
                    direction = 'up'
                else:
                    break
            elif direction == 'up':
                if row - 1 >= 0 and result[row - 1][col] == 0:
                    row -= 1
                elif col + 1 < n and result[row][col + 1] == 0:
                    col += 1
                    direction = 'right'
                else:
                    break

        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.generate_matrix(3)