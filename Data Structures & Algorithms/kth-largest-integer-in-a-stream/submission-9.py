class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [-3000]
        for num in nums:
            self.insert(num)
        for pop in range(len(self.heap)-k-1):
            self.pop()
        return 

    def insert(self, num):
        self.heap.append(num)
        i = len(self.heap) - 1
        while i > 1:
            p = i//2
            if self.heap[p] > self.heap[i]:
                t = self.heap[p]
                self.heap[p] = self.heap[i]
                self.heap[i] = t
                i = p
                continue 
            return
    
    def pop(self):
        if len(self.heap)  < 2:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()    
        res = self.heap[1]
        self.heap[1] = self.heap.pop()

        p = 1
        while p*2 < len(self.heap):
            # because heap can't have right child without left child 
            c = -1
            goRight =              (p*2)+1  < len(self.heap) \
                     and self.heap[(p*2)+1] < self.heap[p*2] \
                     and self.heap[(p*2)+1] < self.heap[p]

            goLeft = not goRight                        \
                     and           p*2 < len(self.heap) \
                     and self.heap[p*2] < self.heap[p]

            if   goRight:
                c = (p*2)+1
            elif goLeft:
                c =  p*2
            else:
                break
            t = self.heap[p]
            self.heap[p] = self.heap[c]
            self.heap[c] = t
            p = c
        return res
        

    def add(self, val: int) -> int:

        if len(self.heap) <= self.k:
            self.insert(val)
        else:
            if val > self.heap[1]:
                self.pop()
                self.insert(val)
        
        return self.heap[1]



