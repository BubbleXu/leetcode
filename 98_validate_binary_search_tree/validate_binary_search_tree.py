# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.
# Example 1:
#     2
#    / \
#   1   3
# Binary tree [2,1,3], return true.
# Example 2:
#     1
#    / \
#   2   3
# Binary tree [1,2,3], return false.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def is_valid_BST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.order = []
        self.result = True
        self.in_order(root)
        return self.result

    def in_order(self, root):
        if root is not None:
            self.in_order(root.left)
            if not self.result:
                return

            if len(self.order) == 0 or self.order[-1] < root.val:
                self.order.append(root.val)
            else:
                self.result = False
                return

            self.in_order(root.right)


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1)
    root.right = TreeNode(12)
    print solution.is_valid_BST(root)

