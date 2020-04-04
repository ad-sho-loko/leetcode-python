# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode(0)
        top = head

        front = []
        for i, n in enumerate(lists):
            if n is not None:
                front.append((n.val, i, n))
        heapq.heapify(front)

        while True:
            if len(front) == 0:
                break

            # 最小の先頭値を取得
            _, i, n = heapq.heappop(front)

            if n.next is not None:
                heapq.heappush(front, (n.next.val, i, n.next))

            head.next = n
            head = head.next

        return top.next
