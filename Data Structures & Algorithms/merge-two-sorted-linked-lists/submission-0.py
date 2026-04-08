# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def iter_linkedlist(self, head):
        curr = head
        while curr:
            yield curr
            curr = curr.next

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            start = l1
            l1 = l1.next
        else:
            start = l2
            l2 = l2.next
        curr = start
        while l1 != None or l2 != None:
            if l1 and l2 and l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            elif l1 and l2 and l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            elif l1:
                curr.next = l1
                break
            else:
                curr.next = l2
                break
            curr = curr.next
        return start