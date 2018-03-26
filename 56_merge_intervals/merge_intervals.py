# Given a collection of intervals, merge all overlapping intervals.
#
# For example,
# Given [1,3],[2,6],[8,10],[15,18],
# return [1,6],[8,10],[15,18].


# Definition for an interval.
import copy


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []

        result = [intervals[0]]
        for i in range(1, len(intervals)):
            tmp_result = []
            cur = intervals[i]
            while len(result) > 0:
                pre = result.pop(0)
                if cur.end < pre.start or cur.start > pre.end:
                    tmp_result.append(pre)
                else:
                    cur.start = min(cur.start, pre.start)
                    cur.end = max(cur.end, pre.end)
            tmp_result.append(cur)
            result = copy.deepcopy(tmp_result)
        return result

    def merge2(self, intervals):
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x.start)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if result[-1].end < intervals[i].start:
                result.append(intervals[i])
            else:
                result[-1].end = max(intervals[i].end, result[-1].end)
        return result


if __name__ == '__main__':
    solution = Solution()
    intervals = [Interval(1, 4), Interval(2, 3), Interval(8, 10), Interval(15, 18)]
    print solution.merge2(intervals)
