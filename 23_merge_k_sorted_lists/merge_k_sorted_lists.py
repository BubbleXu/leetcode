# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def merge_k_lists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype ListNode
        """
        if len(lists) == 0:
            return None

        if len(lists) == 1:
            return lists[0]

        nums = []
        for i in range(len(lists)):
            cur = lists[i]
            while cur:
                nums.append(cur.val)
                cur = cur.next

        nums.sort()
        dummy = ListNode(0)
        cur = dummy
        for x in nums:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next