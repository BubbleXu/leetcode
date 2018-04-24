# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.values = []
        self.in_order(root)
        self.cur_index = -1

    def hasNext(self):
        """
        :rtype: bool
        """
        next_index = self.cur_index + 1
        return next_index < len(self.values)

    def next(self):
        """
        :rtype: int
        """
        self.cur_index += 1
        return self.values[self.cur_index]

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            self.values.append(root.val)
            self.in_order(root.right)


class BSTIterator2(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.push_lefts(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) > 0

    def next(self):
        """
        :rtype: int
        """
        top = self.stack.pop(-1)
        self.push_lefts(top.right)
        return top.val

    def push_lefts(self, node):
        while node:
            self.stack.append(node)
            node = node.left

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())