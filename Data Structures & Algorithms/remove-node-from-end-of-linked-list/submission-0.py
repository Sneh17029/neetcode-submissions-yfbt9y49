# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        d = ListNode(0, head)
        f = d
        while n!=0:
            f = f.next
            n -= 1
        s = d
        while f.next != None:
            f = f.next
            s = s.next
        s.next = s.next.next
        return d.next