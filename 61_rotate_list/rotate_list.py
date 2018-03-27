# Given a list, rotate the list to the right by k places, where k is non-negative.
#
# Example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return head

        # count the length
        # k = k % length
        length = 0
        cur = head
        while cur is not None:
            cur = cur.next
            length += 1
        k = k % length
        if k == 0:
            return head

        fast = head
        slow = head
        while k > 0 and fast.next is not None:
            fast = fast.next
            k -= 1

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        fast.next = head
        head = slow.next
        slow.next = None
        return head


