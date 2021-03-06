# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.


class Solution(object):
    def max_area(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(area, result)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    height = [3, 2, 4, 1]
    print solution.max_area(height)