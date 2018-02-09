# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

# convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR"


class Solution(object):
    def convert(self, s, num_rows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if num_rows == 1:
            return s

        space = [[] for _ in range(num_rows)]
        i = 0
        down = False
        for c in s:
            space[i].append(c)
            if down:
                i = i - 1
                if i == 0:
                    down = False
            else:
                i = i + 1
                if i == num_rows - 1:
                    down = True

        result = ''
        for row in space:
            result += ''.join(row)
        return result


if __name__ == '__main__':
    solution = Solution()
    s = 'ABA'
    print solution.convert(s, 2)
