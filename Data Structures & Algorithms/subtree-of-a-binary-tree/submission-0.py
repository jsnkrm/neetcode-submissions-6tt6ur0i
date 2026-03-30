# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.check = False

        def dfs(parent, sub):
            if not parent and not sub:
                return True
            if parent and sub and parent.val == sub.val:
                return dfs(parent.left, sub.left) and dfs(parent.right, sub.right)
            else:
                return False
        
        roots = [root]

        while roots:
            curr = roots.pop(0)

            self.check = dfs(curr, subRoot)
            if self.check:
                return True
            if curr.left:
                roots.append(curr.left)
            if curr.right:
                roots.append(curr.right)
        
        return self.check