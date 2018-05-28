# encoding: utf-8
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
#
# Example 1:
#
# Input: root = [3,1,4,null,2], k = 1
# Output: 1
# Example 2:
#
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# Output: 3


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.result = None
        self.count = 0
        self.in_order(root, k)
        return self.result

    def in_order(self, root, k):
        if root:
            self.in_order(root.left, k)
            if self.result is not None:
                return

            self.count += 1
            if self.count == k:
                self.result = root.val
                return

            self.in_order(root.right, k)


