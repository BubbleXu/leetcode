# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def add_two_numbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        cur_node = dummy_head
        carry = 0
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + carry
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            cur_node.next = ListNode(val)
            cur_node = cur_node.next

            l1 = l1.next
            l2 = l2.next

        l_left = l1 if l1 is not None else l2
        while l_left is not None:
            if carry == 0:
                while l_left is not None:
                    cur_node.next = ListNode(l_left.val)
                    cur_node = cur_node.next
                    l_left = l_left.next
                break

            val = l_left.val + carry
            if val >= 10:
                carry = 1
                val -= 10
            else:
                carry = 0
            cur_node.next = ListNode(val)
            cur_node = cur_node.next

            l_left = l_left.next

        if carry == 1:
            cur_node.next = ListNode(1)

        return dummy_head.next


if __name__ == '__main__':
    solution = Solution()
    l1_head = ListNode(2)
    l1_head.next = ListNode(4)
    l1_head.next.next = ListNode(3)
    l2_head = ListNode(5)
    l2_head.next = ListNode(6)
    l2_head.next.next = ListNode(4)
    result = solution.add_two_numbers(l1_head, l2_head)
    while result is not None:
        print result.val,
        result = result.next




