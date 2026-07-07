"""
# Definition for a Node.
from os import O_LARGEFILE
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # oldNodeStack = []
        # newNodeStack = []
        oldNewMap = { None: None } # None対策

        oldNode = head
        while oldNode:
            newNode = Node(0)

            oldNewMap[oldNode] = newNode
            # oldNodeStack.append(oldNode)
            # newNodeStack.append(newNode)

            oldNode = oldNode.next

        # newHead = None
        oldNode = head # No need Stack
        while oldNode:
            newNode = oldNewMap[oldNode] # No need Stack

            # oldNode = oldNodeStack.pop()
            # newNode = newNodeStack.pop()

            newNode.val    = oldNode.val
            newNode.next   = oldNewMap.get(oldNode.next)
            newNode.random = oldNewMap.get(oldNode.random)

            # newHead = newNode
            oldNode = oldNode.next

        # return newHead
        return oldNewMap[head]
