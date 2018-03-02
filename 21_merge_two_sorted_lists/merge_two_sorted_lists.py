# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge_two_lists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        dummy = ListNode(0)
        cur = dummy
        while cur1 and cur2:
            if cur1.val < cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        left = cur1 if cur1 is not None else cur2
        cur.next = left
        return dummy.next

    def show_list(self, head):
        cur = head
        while cur:
            print str(cur.val) + '->',
            cur = cur.next
        print None


if __name__ == '__main__':
    solution = Solution()
    l1_head = ListNode(1)
    l1_head.next = ListNode(2)
    l1_head.next.next = ListNode(4)
    l2_head = ListNode(1)
    l2_head.next = ListNode(3)
    l2_head.next.next = ListNode(4)

    solution.show_list(l1_head)
    solution.show_list(l2_head)
    head = solution.merge_two_lists(l1_head, l2_head)
    solution.show_list(head)
