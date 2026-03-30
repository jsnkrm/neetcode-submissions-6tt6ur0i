# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
     
        def dfs(root, leftBound, rightBound):
            if root is None: return True
            if leftBound < root.val and root.val < rightBound:
                return (dfs(root.left, leftBound, root.val) 
                        and dfs(root.right, root.val, rightBound))
            else: return False
        
        return dfs(root,float("-inf"),float("inf"))