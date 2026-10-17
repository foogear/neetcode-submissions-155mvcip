# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):, get_args
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def getMiddleNtail(head):
            L, R = head, head
            # list Length < 2 可能なので
            # while R.next.next　やめた
            while R.next:
                L = L.next
                if R.next.next:
                    R = R.next.next
                else:
                    R = R.next

            return (L, R)

        def reverseLL(start):
            # reverse linked list
            # not included start
            prev = start
            curr = start.next

            while curr:
                next = curr.next
                # reverse list
                curr.next = prev
                prev = curr
                curr = next

        def reorder(head, tail):
            L, R = head, tail

            while L.next != R and L != R:
                nextL, nextR = L.next, R.next

                L.next, R.next = R, nextL

                L, R = nextL, nextR
                
        middle, tail = getMiddleNtail(head)
        reverseLL(middle)

        reorder(head, tail)
        middle.next = None