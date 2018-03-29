# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"

class Solution(object):
    def simplify_path(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        stack = []
        for x in path:
            if x == '' or x == '.':
                continue
            elif x == '..':
                if len(stack) > 0:
                    stack.pop(-1)
            else:
                stack.append(x)

        result = '/'.join(stack)
        return '/' + result


if __name__ == '__main__':
    solution = Solution()
    path = '/home//foo/'
    print solution.simplify_path(path)
