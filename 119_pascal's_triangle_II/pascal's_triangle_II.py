# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?


class Solution(object):
    def get_row(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1 for _ in range(rowIndex + 1)]
        for i in range(2, rowIndex + 1):
            for j in reversed(range(1, i)):
                result[j] += result[j - 1]
        return result


if __name__ == '__main__':
    solution = Solution()
    print solution.get_row(4)
