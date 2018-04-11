# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.pre = None
        self.in_order(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)

            if self.pre is not None:
                if self.first is None and self.pre.val >= root.val:
                    self.first = self.pre

                if self.first is not None and self.pre.val >= root.val:
                    self.second = root
            self.pre = root

            self.in_order(root.right)
