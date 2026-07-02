# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, l, e):
        prev = None
        s = l
        while l != e:
            curr = l
            l = l.next
            curr.next = prev
            prev = curr
        return prev, s

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        nxt = head
        prev = nxt
        x = 0
        nl = []
        while nxt:
            x += 1
            nxt = nxt.next
            if x == k:
                x = 0
                nl.append(self.reverseList(prev, nxt))
                prev = nxt
        if x != 0:
            nl.append([prev, None])
        for i in range(len(nl)):
            if i + 1 < len(nl):
                nl[i][1].next = nl[i+1][0]
        return nl[0][0] 