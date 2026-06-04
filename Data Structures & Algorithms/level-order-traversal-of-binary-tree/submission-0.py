# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        visited = [[root]]
        visited_res = [[root.val]]
        for level in visited:
            if not level:
                visited.pop()
                visited_res.pop()
                break
            visited.append([])
            visited_res.append([])
            q = deque(level)
            while q:
                node = q.popleft()
                if node.left:
                    visited[-1].append(node.left)
                    visited_res[-1].append(node.left.val)
                if node.right:
                    visited[-1].append(node.right)
                    visited_res[-1].append(node.right.val)
        return visited_res