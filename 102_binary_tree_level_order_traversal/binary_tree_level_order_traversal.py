# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its level order traversal as:
# [
#   [3],
#   [9,20],
#   [15,7]
# ]

# Definition for a binary tree node.
import copy


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
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

        return result