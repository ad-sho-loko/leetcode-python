# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        now = dummy

        while not (l1 is None and l2 is None):
            if l2 is None or (l1 is not None and l1.val < l2.val):
                now.next = l1
                now = now.next
                l1 = l1.next
            else:
                now.next = l2
                now = now.next
                l2 = l2.next

        return dummy.next

    def mergeTwoList(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        if l1.val < l2.val:

        self.mergeTwoList(l1, l2)


