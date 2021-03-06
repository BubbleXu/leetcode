# Given a binary tree, find the maximum path sum.
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along
# the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# For example:
# Given the below binary tree,
#
#        1
#       / \
#      2   3
# Return 6.

# Definition for a binary tree node.
# class TreeNode(object):
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.result = 0 if not root else root.val
        self.solve(root)
        return self.result

    # max branch + current mode val
    def solve(self, root):
        if not root:
            return 0

        left = max(self.solve(root.left), 0)
        right = max(self.solve(root.right), 0)
        self.result = max(self.result, left + right + root.val)
        return max(left, right) + root.val
