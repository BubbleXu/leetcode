# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB


class Solution(object):
    def convert_to_title(self, n):
        """
        :type n: int
        :rtype: str
        """
        dict = {i: chr(ord('A') + i) for i in range(26)}
        result = []
        while n > 0:
            q, r = divmod(n - 1, 26)
            result.append(dict[r])
            n = q
        return ''.join(reversed(result))


if __name__ == '__main__':
    solution = Solution()
    print solution.convert_to_title(2)
