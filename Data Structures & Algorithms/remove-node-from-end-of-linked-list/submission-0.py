# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        L, R = head, head
        for _ in range(n):
            R = R.next

        # while R.next:
        while R and R.next: # headを削除特別ケース
            R = R.next
            L = L.next

        if L == head: # headを削除特別ケース
            if head.next:
                head = head.next
            else:
                head = None
        else:
            # L.next = R     BUG
            L.next = L.next.next

        return head


