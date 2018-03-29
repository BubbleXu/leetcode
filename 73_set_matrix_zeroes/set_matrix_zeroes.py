# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        rows = {}
        cols = {}
        m = len(matrix)
        if m == 0:
            return

        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for row in rows:
            for j in range(n):
                matrix[row][j] = 0

        for col in cols:
            for i in range(m):
                matrix[i][col] = 0
