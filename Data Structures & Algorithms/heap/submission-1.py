class MinHeap:
    
    def __init__(self):
        self.heap = ['D']

    def push(self, val: int) -> None:
        self.heap.append(val)

        c = len(self.heap) - 1
        while c > 1:
            p = c//2
            if self.heap[c] < self.heap[p]:
                t            = self.heap[p]
                self.heap[p] = self.heap[c]
                self.heap[c] = t
                c = p
                continue
            return

    def goDown(self, p):
        while p*2 < len(self.heap):
            goRight =               (p*2)+1  < len(self.heap) \
                      and self.heap[(p*2)+1] < self.heap[p*2] \
                      and self.heap[(p*2)+1] < self.heap[p]
            goLeft  = not goRight \
                      and           p*2  < len(self.heap) \
                      and self.heap[p*2] < self.heap[p]
            if   goRight:
                c = (p*2)+1
            elif goLeft:
                c = (p*2)
            else:
                break
            t            = self.heap[p]
            self.heap[p] = self.heap[c]
            self.heap[c] = t
            p = c

    def pop(self) -> int:
        if len(self.heap)  < 2:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        self.goDown(1)
        return res

    def top(self) -> int:
        if len(self.heap) < 2:
            return -1
        return self.heap[1]
        
    def heapify(self, nums: List[int]) -> None:
        if len(nums) < 1:
            self.heap = ['D']
            return 
        nums.append(nums[0])
        nums[0] = 'D'
        self.heap = nums
        p = len(nums) - 1
        while p > 0:
            self.goDown(p)
            p -= 1
        return