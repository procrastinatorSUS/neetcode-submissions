# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        tail = head
        ln = 0
        while tail:
            ln += 1
            tail = tail.next

        path = ln - n

        tail = prew = head
        if path == 0:
            return head.next
        else:
            while path:
                prew = tail
                tail = tail.next
                path -= 1
            prew.next = tail.next
            
            return head
