# Given a digit string, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below.

# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


class Solution(object):
    def letter_combinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        result = []
        if len(digits) == 0:
            return result

        if len(digits) == 1:
            for c in dict.get(digits[0]):
                result.append(c)
            return result

        sub_result = self.letter_combinations(digits[1:])
        for c in dict.get(digits[0]):
            for s in sub_result:
                result.append(c + s)
        return result



if __name__ == '__main__':
    solution = Solution()
    digits = '23'
    print solution.letter_combinations(digits)

