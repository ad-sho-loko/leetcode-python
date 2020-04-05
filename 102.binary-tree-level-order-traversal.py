# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class List:
    def __init__(self):
        pass

# おそい。
class Solution:
    ans = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(depth:int, node: TreeNode):
            if node is None:
                return

            if depth == len(self.ans):
                self.ans.append([])

            self.ans[depth].append(node.val)
            dfs(depth + 1, node.left)
            dfs(depth + 1, node.right)

        if not root:
            return []

        dfs(0, root)
        return self.ans




