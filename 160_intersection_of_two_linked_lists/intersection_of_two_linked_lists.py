# encoding: utf-8
# Write a program to find the node at which the intersection of two singly linked lists begins.
#
#
# For example, the following two linked lists:
#
# A:          a1 → a2
#                    ↘
#                      c1 → c2 → c3
#                    ↗
# B:     b1 → b2 → b3
# begin to intersect at node c1.
#
#
# Notes:
#
# If the two linked lists have no intersection at all, return null.
# The linked lists must retain their original structure after the function returns.
# You may assume there are no cycles anywhere in the entire linked structure.
# Your code should preferably run in O(n) time and use only O(1) memory.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        len_1, len_2 = 0, 0
        p1, p2 = headA, headB
        while p1:
            len_1 += 1
            p1 = p1.next
        while p2:
            len_2 += 1
            p2 = p2.next

        p1 = headA
        p2 = headB
        if len_1 > len_2:
            gap = len_1 - len_2
            while gap > 0:
                p1 = p1.next
                gap -= 1
        elif len_1 < len_2:
            gap = len_2 - len_1
            while gap > 0:
                p2 = p2.next
                gap -= 1

        while p1:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
        return None
