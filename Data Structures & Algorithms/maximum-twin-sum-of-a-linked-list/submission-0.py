# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 前半リストmemoするためこう書くしかなかった
        memo = [head.val]
        l = head
        r = head
        while r.next.next:
            l = l.next
            r = r.next.next
            memo.append(l.val)

        res = 0
        l = l.next
        for i in range(len(memo) - 1, -1, -1):
            res = max(res, memo[i] + l.val)
            l = l.next

        return res


