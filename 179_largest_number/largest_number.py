# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largest_number(self, nums):
        if not nums:
            return ''

        candidates = map(str, nums)
        candidates.sort(cmp=lambda x, y: cmp(y + x, x + y))
        return '0' if candidates[0] == '0' else ''.join(candidates)


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 30, 34, 5, 9]
    print solution.largest_number([3, 30, 34, 5, 9])
