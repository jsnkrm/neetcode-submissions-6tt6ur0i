# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.check = True

        def dfs(curr):
            if not curr:
                return [0,0]
            
            left, right = dfs(curr.left)[0] + 1 , dfs(curr.right)[1] + 1
            if abs(left - right) > 1:
                self.check = False
            
            return [max(left , right), max(left , right)]

        dfs(root)
        return self.check