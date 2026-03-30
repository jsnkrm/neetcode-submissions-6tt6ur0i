# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p, q = head, head

        while p and p.next:
            p = p.next.next
            q = q.next
            if p == q:
                return True
           

        return False