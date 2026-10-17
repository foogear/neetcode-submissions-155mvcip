# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getCarryNsum(num1, num2, carry):
            sum = num1 + num2 + carry
            carry = 0
            if sum - 10 >= 0:
                sum -= 10
                carry = 1

            return (carry, sum)

        res = ListNode(-1, None)

        curr, carry, sum = res, 0, 0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            # print(f"{num1} + {num2} + ({carry})")
            carry, sum = getCarryNsum(num1, num2, carry)
            # print(f"{carry}   {sum}")
            # print()
            next = ListNode(sum, None)
            curr.next = next
            curr = next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            curr.next = ListNode(carry, None)
            
        return res.next