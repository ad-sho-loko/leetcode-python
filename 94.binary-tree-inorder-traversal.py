# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        nodes = []

        def traversal(node: TreeNode):
            if node is None:
                return

            nodes.append(node.val)
            traversal(node.left)
            traversal(node.right)

        traversal(root)
        return nodes
