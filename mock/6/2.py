# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        x_parents = self.search(root, [], x)
        y_parents = self.search(root, [], y)

        return x_parents is not None and y_parents is not None and \
               len(x_parents) == len(y_parents) and len(x_parents) > 1 and x_parents[-1] == y_parents[-1]

    def search(self, root: TreeNode, parents: List[int], v: int):
        if root is None:
            return None

        if root.val == v:
            return parents

        parents.append(root.val)

        result = self.search(root.left, parents, v)
        if result is not None:
            return result

        result = self.search(root.right, parents, v)
        return result
