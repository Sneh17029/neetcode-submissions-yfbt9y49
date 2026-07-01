"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        m = {}
        h = head
        x = Node(0)
        l = x
        while h:
            l.next = Node(h.val)
            l = l.next
            m[h] = l
            h = h.next
        h = head
        l = x.next
        while h:
            l.random = m.get(h.random)
            l = l.next
            h = h.next
        return x.next