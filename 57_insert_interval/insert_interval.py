# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
# Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
#
# Example 2:
# Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
#
# This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return [newInterval]

        result = []
        merged = False
        for i in range(len(intervals)):
            cur = intervals[i]
            if cur.end < newInterval.start:
                result.append(cur)
            elif cur.start > newInterval.end:
                result.append(newInterval)
                merged = True
                for j in range(i, len(intervals)):
                    result.append(intervals[j])
                break
            else:
                newInterval.start = min(newInterval.start, cur.start)
                newInterval.end = max(newInterval.end, cur.end)

        if not merged:
            result.append(newInterval)

        return result


if __name__ == '__main__':
    solution = Solution()
    intervals = [Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)]
    print solution.insert(intervals, Interval(4, 9))
