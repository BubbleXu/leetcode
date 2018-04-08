# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# For example,
# Given 1->1->2, return 1->2.
# Given 1->1->2->3->3, return 1->2->3.
#


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        slow = head
        fast = slow.next
        repeated = False
        while fast is not None:
            if slow.val == fast.val:
                fast = fast.next
                repeated = True
            else:
                if repeated:
                    slow.next = fast
                    slow = fast
                    fast = fast.next
                    repeated = False
                else:
                    slow = fast
                    fast = fast.next

        if repeated:
            slow.next= None

        return head