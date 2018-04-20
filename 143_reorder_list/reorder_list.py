# coding: utf-8
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # break into two lists
        slow, fast = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None

        # reverse the second list
        head2 = self.reverse(head2)

        # merge two lists
        dummy = ListNode(0)
        cur = dummy
        cur1, cur2 = head, head2
        while cur1 and cur2:
            cur.next = cur1
            cur1 = cur1.next
            cur = cur.next

            cur.next = cur2
            cur2 = cur2.next
            cur = cur.next

        if cur1:
            cur.next = cur1

        head = dummy.next

    def reverse(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = head
        cur = pre.next
        while cur:
            pre.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = pre.next
        return dummy.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    solution.reorderList(head)

