# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        p = [lists[i] for i in range(len(lists))]
        count = 0
        for i in range(len(lists)):
            curr = lists[i]
            while curr:
                curr = curr.next
                count += 1
        
        res = ListNode()
        curr = res
        for i in range(count):
            minVal = 1001
            minIndex = -1
            for j in range(0, len(lists)):
                if p[j] and p[j].val < minVal:
                    minIndex = j
                    minVal = min(minVal, p[j].val)
            if minIndex != -1 and minVal != 1001:
                p[minIndex] = p[minIndex].next
                curr.next = ListNode(minVal)
                curr = curr.next
        return res.next