# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # ポイント1: left, rightを取るメソッドに切り出せるか
    # ポイント2: 深さ3以降のleft, rightは図示したときに隣り合うノードではないこと。
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(left: TreeNode, right: TreeNode):
            if left is None and right is None:
                return True

            if left is None or right is None:
                return False

            return left.val == right.val \
                   and isMirror(left.right, right.left) \
                   and isMirror(left.left, right.right)

        if root is None:
            return True

        return isMirror(root.left, root.right)
