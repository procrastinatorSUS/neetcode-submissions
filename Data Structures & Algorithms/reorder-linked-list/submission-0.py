# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        middle = slow.next
        slow.next = None

        prew = None
        while middle:
            between = middle.next
            middle.next = prew
            prew = middle
            middle = between
        head_r = prew
        tail = head
        
        while head_r:
            next_head_r = head_r.next
            next_tail = tail.next

            tail.next = head_r
            head_r.next = next_tail

            tail = next_tail
            head_r = next_head_r
