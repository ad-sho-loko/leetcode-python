class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        # [1] 多重代入が可能
        # [2] ダミーで入れることで最初のNone.nextを避けることができる
        now = root = ListNode(0)

        while l1 or l2 or carry:
            v1 = 0
            v2 = 0
            if l1 is not None:
                v1 = l1.val
                l1 = l1.next
            if l2 is not None:
                v2 = l2.val
                l2 = l2.next

            v = v1 + v2 + carry
            if v >= 10:
                v -= 10
                carry = 1
            else:
                carry = 0

            now.next = ListNode(v)
            now = now.next

        # ダミーなので次ポインタを入れておく
        return root.next
