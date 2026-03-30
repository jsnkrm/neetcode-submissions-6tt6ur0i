# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = [root]

        while q:
            qLen = len(q)
            last = TreeNode(-1)
            for i in range(qLen):
                curr = q.pop(0)
                if curr:
                    last = curr
                    q.append(curr.left)
                    q.append(curr.right)
            if last.val != -1:
                res.append(last.val)
        return res
            