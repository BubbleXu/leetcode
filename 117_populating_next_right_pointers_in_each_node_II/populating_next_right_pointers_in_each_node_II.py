# Follow up for problem "Populating Next Right Pointers in Each Node".
#
# What if the given tree could be any binary tree? Would your previous solution still work?
#
# Note:
#
# You may only use constant extra space.
# For example,
# Given the following binary tree,
#          1
#        /  \
#       2    3
#      / \    \
#     4   5    7
# After calling your function, the tree should look like:
#          1 -> NULL
#        /  \
#       2 -> 3 -> NULL
#      / \    \
#     4-> 5 -> 7 -> NULL


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        cur_queue = []
        if root is not None:
            cur_queue.append(root)

        while cur_queue:
            next_queue = []
            while cur_queue:
                cur = cur_queue.pop(0)
                if cur_queue:
                    cur.next = cur_queue[0]
                else:
                    cur.next = None

                if cur.left is not None:
                    next_queue.append(cur.left)
                if cur.right is not None:
                    next_queue.append(cur.right)

            cur_queue = next_queue