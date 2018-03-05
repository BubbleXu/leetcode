# Given a linked list, swap every two adjacent nodes and return its head.
#
# For example,
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Your algorithm should use only constant space.
# You may not modify the values in the list, only nodes itself can be changed.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_k_group(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        first = pre.next
        if first is None:
            return dummy.next
        last = first
        for _ in range(k - 1):
            last = last.next
            if last is None:
                return dummy.next

        while True:
            cur_head = self.reverse(first, last.next)
            pre.next = cur_head

            pre = first
            first = pre.next
            if first is None:
                return dummy.next
            last = first
            for _ in range(k - 1):
                last = last.next
                if last is None:
                    return dummy.next

    def reverse(self, head, tail):
        dummy = ListNode(0)
        dummy.next = head
        pre = head
        cur = pre.next
        while cur != tail:
            pre.next = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = pre.next
        return dummy.next

    def show_list(self, head):
        cur = head
        while cur:
            print str(cur.val) + '->',
            cur = cur.next
        print None


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(1)
    cur = head
    for i in range(2, 6):
        cur.next = ListNode(i)
        cur = cur.next
    solution.show_list(head)
    head = solution.reverse_k_group(head, 2)
    solution.show_list(head)