# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.


class Solution(object):
    def num_decodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0

        double_end = 0
        if 1 <= int(s[0]) <= 9:
            single_end = 1
        else:
            return 0

        for i in range(1, len(s)):
            last_single_end = single_end
            if 1 <= int(s[i]) <= 9:
                single_end += double_end
            else:
                single_end = 0

            if 10 <= int(s[i-1: i+1]) <= 26:
                double_end = last_single_end
            else:
                double_end = 0

        return single_end + double_end

        # if len(s) == 0:
        #     return 0

        # self.count = 0
        # self.solve(s)
        # return self.count

    def solve(self, s):
        if len(s) == 0:
            self.count += 1
            return

        if 1 <= int(s[0]) <= 9:
            self.solve(s[1:])

        if len(s) > 1 and 10 <= int(s[:2]) <= 26:
            self.solve(s[2:])


if __name__ == '__main__':
    solution = Solution()
    print solution.num_decodings('1220')
