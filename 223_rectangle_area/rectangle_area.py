# Find the total area covered by two rectilinear rectangles in a 2D plane.
# Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
#
# Rectangle Area
#
# Example:
#
# Input: -3, 0, 3, 4, 0, -1, 9, 2
# Output: 45

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        s1 = (C - A) * (D - B)
        s2 = (G - E) * (H - F)
        left_down = (max(A, E), max(B, F))
        right_up = (min(C, G), min(D, H))
        s3 = 0
        if left_down[0] < right_up[0] and left_down[1] < right_up[1]:
            s3 = (right_up[0] - left_down[0]) * (right_up[1] - left_down[1])
        return s1 + s2 - s3


if __name__ == '__main__':
    solution = Solution()
    print solution.computeArea(-3, 0, 3, 4, 0, -1, 9, 2)