class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val != q.val:
                return False
            else:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
        if root is None:
            return False
        elif root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)