# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, val):
            if not root:
                return 0
            if root.val >= val:
                return dfs(root.left, root.val) + dfs(root.right, root.val) + 1
            return dfs(root.left, val) + dfs(root.right, val)
            
        return dfs(root, root.val)
