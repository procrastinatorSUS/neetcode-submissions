# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

            
        def check_nodes(root, l, r):
            if not root:
                return True

            if root.left:
                if root.left.val < root.val and root.left.val > r:
                    pass
                else:
                    return False
                
            if root.right:
                if root.right.val > root.val and root.right.val < l:
                    pass
                else:
                    return False
            return check_nodes(root.left, root.val, r) and check_nodes(root.right, l, root.val)


        return check_nodes(root, float("inf"), -float("inf"))
        