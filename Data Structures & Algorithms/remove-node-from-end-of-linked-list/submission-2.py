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

        # head指す = head削除　これは間違い⭐⭐⭐
        if L == head and not R: # head指す　かつ　head削除
            if head.next:
                head = head.next
            else:            
                head = None
        else:                   # head指してるが  head削除とは限らないので
            # L.next = R     BUG
            L.next = L.next.next

        return head


