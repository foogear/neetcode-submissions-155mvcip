# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l, r = head.next, head.next
        prev = head
        while r.next:
            r = r.next.next
            # swap
            curr = l
            l = curr.next
            curr.next = prev
            prev = curr

        # 1 <= 2 <= 3 | 4 => 5 => 6
        r, l = l, prev
        res = 0
        while r:
            res = max(res, l.val + r.val)
            l = l.next
            r = r.next

        return res



