# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie, from left to right, level by level from leaf to root).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its bottom-up level order traversal as:
# [
#   [15,7],
#   [9,20],
#   [3]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        cur_queue = []
        if root is not None:
            cur_queue.append(root)

        while cur_queue:
            level = []
            next_queue = []
            while cur_queue:
                cur = cur_queue.pop(0)
                level.append(cur.val)
                if cur.left is not None:
                    next_queue.append(cur.left)
                if cur.right is not None:
                    next_queue.append(cur.right)
            result.append(level)
            cur_queue = [x for x in next_queue]

        result.reverse()
        return result