"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':


        oldNodeStack = []
        newNodeStack = []
        oldNewMap = {}
        
        

        
        oldNode = head
        while oldNode:
            newNode = Node(0)
            oldNewMap[oldNode] = newNode
            oldNodeStack.append(oldNode)
            newNodeStack.append(newNode)
            oldNode = oldNode.next


        newHead = None
        while oldNodeStack:
            oldNode = oldNodeStack.pop()
            newNode = newNodeStack.pop()

            newNode.val    = oldNode.val
            newNode.next   = oldNewMap.get(oldNode.next)
            newNode.random = oldNewMap.get(oldNode.random)
            

            newHead = newNode

        return newHead
















