# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        c = None
        n = head
        an = head.next
        while n:
            n.next = c
            c = n
            n = an
            if an:
                an = an.next
            else:
                an = None
        return c