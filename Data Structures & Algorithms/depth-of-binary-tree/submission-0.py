# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    ma = 0
    curr = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        self.curr += 1
        self.ma = max(self.ma, self.curr)
        self.maxDepth(root.left)
        self.maxDepth(root.right)
        self.curr -= 1
        return self.ma