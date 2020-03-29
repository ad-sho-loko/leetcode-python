# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        front = head
        for _ in range(n):
            front = front.next

        # リスト長さ == nの場合、prevがNoneのまま来てしまうの対策
        prev = head.next
        cur = head

        while front is not None:
            prev = cur
            cur = cur.next
            front = front.next

        prev.next = cur.next
        return head
