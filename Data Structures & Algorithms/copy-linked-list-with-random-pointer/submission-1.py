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
        if not(head):
            return None
        dc_table = dict()
        tail = last = head
        prew = None
        
        while tail: 
            dc_table[tail] = Node(x = tail.val, next = prew)
            prew = dc_table[tail]
            last = tail
            tail = tail.next
        tail = head
        while tail:
            if tail.random:
                dc_table[tail].random = dc_table[tail.random]
            else:
                dc_table[tail].random = None
            tail = tail.next
        dc_curr = dc_table[last]
        prew = None
        while dc_curr:
            btw = dc_curr.next
            dc_curr.next = prew
            prew = dc_curr
            dc_curr = btw
        return prew