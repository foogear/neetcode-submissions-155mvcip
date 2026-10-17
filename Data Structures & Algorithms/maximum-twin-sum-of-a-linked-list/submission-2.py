# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l, r = head, head
        while r.next.next:
            l = l.next
            r = r.next.next
        m = l
        l = l.next
        r = l.next
        while r:
            curr = r
            r = r.next
            curr.next = l
            l = curr
        m.next.next = None
        m.next = l

        l = head
        r = m.next
        res = 0
        while r:
            res = max(res, l.val + r.val)
            l, r = l.next, r.next

        return res



