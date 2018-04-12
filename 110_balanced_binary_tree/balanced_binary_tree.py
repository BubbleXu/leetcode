# Given a binary tree, determine if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as:
# a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example 1:
# Given the following tree [3,9,20,null,null,15,7]:
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# Return true.
#
# Example 2:
# Given the following tree [1,2,2,3,3,null,null,4,4]:
#
#        1
#       / \
#      2   2
#     / \
#    3   3
#   / \
#  4   4
# Return false.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.result = True
        self.max_depth(root)
        return self.result

    def max_depth(self, root):
        if root is None:
            return 0

        left_max_depth = self.max_depth(root.left)
        right_max_depth = self.max_depth(root.right)
        if abs(right_max_depth - left_max_depth) > 1:
            self.result = False
        return max(left_max_depth, right_max_depth) + 1