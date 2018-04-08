# Given a linked list and a value x,
# partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
# For example,
# Given 1->4->3->2->5->2 and x = 3,
# return 1->2->2->4->3->5.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        l1_head = ListNode(0)
        l1_cur = l1_head
        l2_head = ListNode(0)
        l2_cur = l2_head
        cur = head
        while cur is not None:
            if cur.val < x:
                l1_cur.next = cur
                l1_cur = l1_cur.next
            else:
                l2_cur.next = cur
                l2_cur = l2_cur.next

            cur = cur.next

        l1_cur.next = l2_head.next
        l2_cur.next = None
        return l1_head.next


if __name__ == '__main__':
    solution = Solution()
    head = ListNode(2)
    head.next = ListNode(1)
    solution.partition(head, 2)