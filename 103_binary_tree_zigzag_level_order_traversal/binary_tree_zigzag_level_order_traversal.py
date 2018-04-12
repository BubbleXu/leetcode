# Given a binary tree, return the zigzag level order traversal of its nodes' values.
# (ie, from left to right, then right to left for the next level and alternate between).
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7
# return its zigzag level order traversal as:
# [
#   [3],
#   [20,9],
#   [15,7]
# ]

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        cur_queue = []
        if root is not None:
            cur_queue.append(root)

        next_direction = 'to_left'
        while cur_queue:
            level = []
            next_queue = []
            while cur_queue:
                cur = cur_queue.pop(0)
                level.append(cur.val)

                if next_direction == 'to_left':
                    if cur.left is not None:
                        next_queue.append(cur.left)
                    if cur.right is not None:
                        next_queue.append(cur.right)
                else:
                    if cur.right is not None:
                        next_queue.append(cur.right)
                    if cur.left is not None:
                        next_queue.append(cur.left)

            result.append(level)
            cur_queue = [x for x in reversed(next_queue)]
            if next_direction == 'to_left':
                next_direction = 'to_right'
            else:
                next_direction = 'to_left'

        return result
