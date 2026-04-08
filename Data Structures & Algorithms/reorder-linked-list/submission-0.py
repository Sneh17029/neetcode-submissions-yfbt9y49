# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = head
        f = head
        while f != None and f.next != None:
            f = f.next.next
            s = s.next
        curr = s.next
        s.next = None
        prev = None
        new = curr
        while curr != None:
            next_curr = curr.next
            curr.next = prev
            prev = curr
            curr = next_curr
        first = head
        second = prev
        while second != None:
            t1 = first.next
            t2 = second.next
            second.next = t1    
            first.next = second
            second = t2
            first = t1