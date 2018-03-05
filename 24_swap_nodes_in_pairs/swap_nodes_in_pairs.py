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
    def swap_pairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        first = pre.next
        if first is None:
            return dummy.next
        second = first.next
        if second is None:
            return dummy.next

        while True:
            pre.next = second
            first.next = second.next
            second.next = first

            pre = first
            first = first.next
            if first is None:
                break
            second = first.next
            if second is None:
                break
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
    head = solution.swap_pairs(head)
    solution.show_list(head)