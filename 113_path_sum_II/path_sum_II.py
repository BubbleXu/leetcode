# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.solve(root, sum, [], result)
        return result

    def solve(self, root, sum, cur, result):
        if root is None:
            return

        if root.left is None and root.right is None and root.val == sum:
            cur.append(root.val)
            result.append(cur)
            return

        self.solve(root.left, sum - root.val, cur + [root.val], result)
        self.solve(root.right, sum - root.val, cur + [root.val], result)

