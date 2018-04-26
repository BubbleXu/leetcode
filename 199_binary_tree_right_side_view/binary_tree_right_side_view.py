# Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
# ordered from top to bottom.

# For example:
# Given the following binary tree,
#
#    1            <---
#  /   \
# 2     3         <---
#  \     \
#   5     4       <---
#
#
# You should return [1, 3, 4].

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result

        queue = [root]
        while queue:
            next_queue = []
            rightmost = None
            while queue:
                cur = queue.pop(0)
                rightmost = cur.val
                if cur.left:
                    next_queue.append(cur.left)
                if cur.right:
                    next_queue.append(cur.right)
            queue = next_queue
            result.append(rightmost)

        return result