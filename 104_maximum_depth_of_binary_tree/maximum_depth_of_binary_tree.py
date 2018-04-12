# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its depth = 3.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur_queue = []
        level = 0
        if root is not None:
            cur_queue.append(root)

        while cur_queue:
            next_queue = []
            level += 1
            while cur_queue:
                cur = cur_queue.pop(0)
                if cur.left is not None:
                    next_queue.append(cur.left)
                if cur.right is not None:
                    next_queue.append(cur.right)
            cur_queue = next_queue

        return level

    def max_depth(self, root):
        if root is None:
            return 0

        return max(self.max_depth(root.left), self.max_depth(root.right)) + 1
