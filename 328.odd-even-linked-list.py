# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        even = head.next
        even_top = even

        isOdd = True
        now = head.next.next
        even.next = None

        while now is not None:
            nextn = now.next

            if isOdd:
                now.next = even_top
                odd.next = now
                odd = odd.next
            else:
                even.next = now
                even = even.next
                even.next = None

            now = nextn
            isOdd = not isOdd

        return head
