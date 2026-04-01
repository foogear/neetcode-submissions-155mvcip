class Node:

    def __init__(self, val, pre=None, next=None):
        self.val  = val
        self.pre  = pre
        self.next = next


class HashLinkList:

    def __init__(self):
        self.cur   = 0 # Big mistake
        self.lkls  = {0:Node("D")}
        self.index = 0 # Not reusing index

    def push(self, val):
        print("-------------push")
        print(self.cur)
        self.index += 1
        preNode = self.lkls[self.cur]
        self.lkls[self.index] = Node(val, self.cur)
        self.cur = self.index
        preNode.next = self.cur
        return

    def len(self):
        return len(self.lkls) - 1

    def firstNodeIndex(self):
        return self.lkls[0].next

    def pop(self, index):
        print("-------------pop")
        if index not in self.lkls or index == 0:
            return -1
        cur  = self.lkls[index]
        del    self.lkls[index]

        if cur.pre  != None: # When index=0 "if cur.pre:" won't work properly 
            pre  = self.lkls[cur.pre]
            pre.next = cur.next
        if cur.next != None:
            next = self.lkls[cur.next]
            next.pre = cur.pre

        if self.cur == index:# Big mistake
            self.cur = cur.pre
        return cur.val

    def findIndex(self, index):
        if index in self.lkls:
            return True 
        return False 





class LRUCache:

    def __init__(self, capacity: int):
        print("\ninit")
        self.hlkls = HashLinkList()
        self.cap = capacity
        self.map = {}
        self.count = 0

    def printNode(self):
        if self.count <= -1:
            return 
        print("{",end="")
        for k in self.hlkls.lkls:
            n = self.hlkls.lkls[k]
            print(f"{k}:[{n.pre}<={n.val}=>{n.next}], ",end="")
        print("}")
        return 

    def get(self, key: int) -> int:
        self.count += 1
        print("\n******get")
        print(f"map={self.map}")
        print(self.hlkls.cur)
        self.printNode()
        if key not in self.map:
            return -1
        if not self.hlkls.findIndex(self.map[key]):# Forgot that
            del self.map[key]
            return -1
        index = self.map[key]
        val = self.hlkls.pop(index)
        print(self.hlkls.cur)
        self.printNode()
        self.hlkls.push(val)
        self.map[key] = self.hlkls.cur
        self.printNode()
        return val
        

    def put(self, key: int, value: int) -> None:
        self.count += 1
        print("\n******put")
        print(f"map={self.map}")
        print(self.hlkls.cur)
        self.printNode()
        if key in self.map and self.hlkls.findIndex(self.map[key]):
            # val = self.hlkls.pop(self.map[key])
            self.hlkls.pop(self.map[key])
            self.printNode()
            # self.hlkls.push(val) 
            self.hlkls.push(value) # Big mistake we need new val
            self.map[key] = self.hlkls.cur # Forgot this big s**t
            return 
        elif key in self.map:
            del self.map[key]

        if self.hlkls.len() >= self.cap:
            index = self.hlkls.firstNodeIndex()
            self.hlkls.pop(index)
        print(self.hlkls.cur)
        self.printNode()
        self.hlkls.push(value)
        self.map[key] = self.hlkls.cur
        self.printNode()
        return

        
