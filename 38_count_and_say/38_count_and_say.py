# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
#
# Example 1:
# Input: 1
# Output: "1"

# Example 2:
# Input: 4
# Output: "1211"


class Solution(object):
    def count_and_say(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n <= 1:
            return '1'

        cur_result = '1'
        last_count = 0
        last_say = '_'
        next_result = ''
        for _ in range(n - 1):
            # read current str
            for x in cur_result:
                if x == last_say:
                    last_count += 1
                else:
                    if last_count > 0:
                        next_result += str(last_count) + last_say
                    last_count = 1
                    last_say = x
            next_result += str(last_count) + last_say

            cur_result = next_result
            last_count = 0
            last_say = '_'
            next_result = ''

        return cur_result


if __name__ == '__main__':
    solution = Solution()
    print solution.count_and_say(8)
