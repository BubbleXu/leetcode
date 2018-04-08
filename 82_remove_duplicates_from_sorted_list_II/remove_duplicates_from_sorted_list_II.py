# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
#
# For example,
# Given 1->2->3->3->4->4->5, return 1->2->5.
# Given 1->1->1->2->3, return 2->3.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def delete_duplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        slow = head
        fast = slow.next
        repeated = False
        while fast is not None:
            if slow.val == fast.val:
                fast = fast.next
                repeated = True
            else:
                if repeated:
                    pre.next = fast
                    slow = fast
                    fast = fast.next
                    repeated = False
                else:
                    pre = slow
                    slow = fast
                    fast = fast.next

        if repeated:
            pre.next = None

        return dummy.next




