# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, c1: Optional[ListNode], c2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        res = final
        while c1 and c2:
            if c1.val <= c2.val:
                res.next = c1
                c1 = c1.next
            else:
                res.next = c2
                c2 = c2.next
            res = res.next
        res.next = c1 if c1 else c2
        return final.next