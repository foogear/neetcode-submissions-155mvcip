# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def merge(self, l, r):
        s=ListNode()
        curr=s
        while l and r:
            if r.val < l.val:
                curr.next=r
                r=r.next
            else:
                curr.next=l
                l=l.next
            curr=curr.next
        
        if l==None:
            curr.next=r
        if r==None:
            curr.next=l
        
        return s.next




    def mergeKLists(self, lists: List[Optional[ListNode]], l=0, r=-1) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        


        if r<0:
            r=len(lists)-1
        if r==l:
            return lists[r]

        LLists=self.mergeKLists(lists, l, int((l+r)/2))
        RLists=self.mergeKLists(lists,    int((l+r)/2)+1,r)


        return self.merge(LLists,RLists)









