# Given a string containing only digits, restore it by returning all possible valid IP address combinations.
#
# For example:
# Given "25525511135",
#
# return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)


class Solution(object):
    def restore_ip_addresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.solve(s, 4, '', result)
        return result

    def solve(self, s, left, cur, result):
        if len(s) == 0:
            return

        if left == 1:
            if (s[0] == '0' and len(s) > 1) or (int(s) > 255):
                return
            result.append(cur + s)

        if s[0] == '0':
            self.solve(s[1:], left - 1, cur + s[: 1] + '.', result)
        else:
            for i in range(min(3, len(s))):
                if i < 2 or 0 <= int(s[: i+1]) <= 255:
                    self.solve(s[i+1:], left - 1, cur + s[: i+1] + '.', result)


if __name__ == '__main__':
    solution = Solution()
    s = "25525511135"
    print solution.restore_ip_addresses(s)
