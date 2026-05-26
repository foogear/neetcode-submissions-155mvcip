# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        memo = []
        while head:
            memo.append(head.val)
            head = head.next

        res = 0
        memoLen = len(memo)
        for i in range(0, int(memoLen / 2)):
            res = max(res, memo[i] + memo[memoLen - i - 1])

        return res


