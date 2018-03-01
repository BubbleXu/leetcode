# Given a linked list, remove the nth node from the end of list and return its head.
#
# For example,
#
#    Given linked list: 1->2->3->4->5, and n = 2.
#
#    After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note:
# Given n will always be valid.
# Try to do this in one pass.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def remove_nth_from_end(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        fast = head
        for i in range(n):
            fast = fast.next

        while fast:
            pre = pre.next
            cur = cur.next
            fast = fast.next

        pre.next = cur.next
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
    head = solution.remove_nth_from_end(head, 2)
    solution.show_list(head)
