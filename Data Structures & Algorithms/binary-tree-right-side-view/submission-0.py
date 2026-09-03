# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def __init__(self):
        self.g_level = 1
        self.res = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return self.res
        self.res.append(root.val)

        self.find_r(root = root, l_level = 1)
        return self.res

    def find_r(self, root: Optional[TreeNode], l_level:int):

        if root:
            if root.right:
                if l_level+1 > self.g_level:
                    self.res.append(root.right.val)
                    self.g_level = l_level+1
            elif root.left:
                if l_level+1 > self.g_level:
                    self.res.append(root.left.val)
                    self.g_level = l_level+1
            l_level += 1
            return self.find_r(root.right, l_level), self.find_r(root.left, l_level)
