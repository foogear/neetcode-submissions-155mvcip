class MyCalendar:
    
    def __init__(self):
        self.root = TreeNode(None, None, 0, 0)
        
    def book(self, startTime: int, endTime: int) -> bool:
        def insert(startTime, endTime, root):
            if not root:
                return TreeNode(None, None, startTime, endTime)

            if     (root.startTime < startTime < root.endTime
                or (root.startTime < endTime   < root.endTime)):
                return None

            if root.endTime <= startTime:
                root.rightChild = insert(startTime, endTime, root.rightChild)
                return root.rightChild
            elif endTime <= root.startTime:
                root.leftChild  = insert(startTime, endTime, root.leftChild)
                return root.leftChild

        if insert(startTime, endTime, self.root):
            return True
        else:
            return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)

class TreeNode:
    def __init__(self, lc, rc, st, et) -> None:
        self.leftChild  = lc
        self.rightChild = rc
        self.startTime = st
        self.endTime = et

