# A linked list is given such that each node contains an additional random pointer which could point to any node in
# the list or null.
#
# Return a deep copy of the list.


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None

        new_head = RandomListNode(head.label)
        new_cur_node = new_head
        cur_node = head.next
        dict = {new_head.label: new_head}
        while cur_node:
            new_cur_node.next = RandomListNode(cur_node.label)
            new_cur_node = new_cur_node.next
            dict[new_cur_node.label] = new_cur_node
            cur_node = cur_node.next

        cur_node = head
        new_cur_node = new_head
        while cur_node:
            if cur_node.random:
                new_cur_node.random = dict[cur_node.random.label]
            cur_node = cur_node.next
            new_cur_node = new_cur_node.next

        return new_head
