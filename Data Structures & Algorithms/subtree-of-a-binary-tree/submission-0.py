# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, sub):
            if not root and not sub:
                return True
            if not sub or not root:
                return False
            if root.val != sub.val:
                return False
            return dfs(root.left, sub.left) and dfs(root.right, sub.right)
        if not root:
            return False
        return dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)