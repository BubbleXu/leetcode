# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left_min_depth = self.minDepth(root.left)
        right_min_depth = self.minDepth(root.right)
        return left_min_depth + right_min_depth + 1 \
            if left_min_depth == 0 or right_min_depth == 0 else min(left_min_depth, right_min_depth) + 1
