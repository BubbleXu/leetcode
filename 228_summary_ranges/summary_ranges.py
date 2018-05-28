# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        result = []
        cur_start = nums[0]
        cur_end = nums[0]
        for x in nums[1:]:
            if x == cur_end + 1:
                cur_end = x
            else:
                range = str(cur_start) + '->' + str(cur_end) if cur_start != cur_end else str(cur_start)
                result.append(range)
                cur_start = x
                cur_end = x
        range = str(cur_start) + '->' + str(cur_end) if cur_start != cur_end else str(cur_start)
        result.append(range)
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [0,2,3,4,6,8,9]
    print solution.summaryRanges(nums)