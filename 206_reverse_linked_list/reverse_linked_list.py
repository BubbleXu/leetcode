# Reverse a singly linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = head
        cur = head.next
        while cur:
            pre.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = pre.next
        return dummy.next