# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        n = head
        i = 0
        visited = {}
        while n is not None:
            if n in visited.keys():
                return n

            visited[i] = i
            n = n.next

        return None
