# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        tail = head
        ost = 0
        while l1 or l2:
            f = l1.val if l1 else 0
            s = l2.val if l2 else 0
            sm = (f + s) + ost
            res = sm % 10
            ost = sm // 10
            tail.val = res
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or ost:
                tail.next = ListNode(ost)
                tail = tail.next


        return head
