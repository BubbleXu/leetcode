# Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1...n.
#
# For example,
# Given n = 3, your program should return all 5 unique BST's shown below.
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.solve(1, n) if n >= 1 else []

    def solve(self, start, end):
        roots = []
        if start > end:
            roots.append(None)
            return roots

        for i in range(start, end + 1):
            left_roots = self.solve(start, i - 1)
            right_roots = self.solve(i + 1, end)
            for left in left_roots:
                for right in right_roots:
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    roots.append(root)
        return roots
