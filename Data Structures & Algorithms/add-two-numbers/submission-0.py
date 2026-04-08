# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = 0
        n = 0
        dummy = ListNode(0)
        l = dummy
        while l1!=None:
            n += l1.val*(10**x)
            x += 1
            l1 = l1.next
        x = 0
        m = 0
        while l2!=None:
            m += l2.val*(10**x)
            x += 1
            l2 = l2.next
        s = m+n
        s = list(str(s)[::-1])
        for i in s:
            l.next = ListNode(int(i))
            l = l.next
        return dummy.next