# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
# find the area of largest rectangle in the histogram.
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.


class Solution(object):
    def largest_rectangle_area(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in xrange(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

        # self.heights = heights
        # return self.solve(0, len(self.heights) - 1)

    def solve(self, left, right):
        if left > right:
            return 0

        if left == right:
            return self.heights[left]

        min_height = self.heights[left]
        min_height_index = left
        for i in range(left + 1, right + 1):
            if self.heights[i] < min_height:
                min_height = self.heights[i]
                min_height_index = i

        return max((right - left + 1) * min_height,
                   self.solve(left, min_height_index - 1),
                   self.solve(min_height_index + 1, right))


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    solution = Solution()
    print solution.largest_rectangle_area(heights)