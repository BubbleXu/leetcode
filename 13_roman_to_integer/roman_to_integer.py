# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def roman_to_int(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        sum = 0
        i = len(s) - 1
        while i >= 0:
            sum += dict[s[i]]
            if i - 1 >= 0 and (s[i-1:i+1] in ['IV', 'XL', 'CD', 'CM', 'XC', 'IX']):
                sum -= dict[s[i-1]]
                i -= 1
            i -= 1
        return sum


if __name__ == '__main__':
    solution = Solution()
    s = 'MCMXCVI'
    print solution.roman_to_int(s)