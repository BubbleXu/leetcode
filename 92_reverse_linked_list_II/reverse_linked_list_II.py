# coding: utf-8

# Reverse a linked list from position m to n. Do it in-place and in one-pass.
#
# For example:
# Given 1->2->3->4->5->NULL, m = 2 and n = 4,
#
# return 1->4->3->2->5->NULL.
#
# Note:
# Given m, n satisfy the following condition:
# 1 ≤ m ≤ n ≤ length of list.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        pre = head
        cur = pre.next
        count = 1
        while count < m:
            first = first.next
            pre = pre.next
            cur = pre.next
            count += 1

        count = 0
        while count < n - m:
            pre.next = cur.next
            cur.next = first.next
            first.next = cur
            cur = pre.next
            count += 1

        return dummy.next


