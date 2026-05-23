class MyCalendar:
    
    def __init__(self):
        self.root = TreeNode(None, None, 0, 0)
        
    def book(self, startTime: int, endTime: int) -> bool:
        print()
        print()
        print(f"inset{(startTime,endTime)}")
        def insert(startTime, endTime, root):
            if not root:
                print("++")
                print((startTime, endTime))
                canInsert[0] = True
                return TreeNode(None, None, startTime, endTime)


            print("*********")
            print(f"parent{(root.startTime, root.endTime)}")

            # < to <=
            cantInsert = ((root.startTime <= startTime < root.endTime) 
                       or (root.startTime < endTime   < root.endTime) )
            if cantInsert:
                print("here")
                canInsert[0] = False
                return None


            if root.endTime <= startTime:
                print('r')
                root.rightChild = insert(startTime, endTime, root.rightChild)
                # return root.rightChild
                return root
            elif endTime <= root.startTime:
                print('l')
                root.leftChild  = insert(startTime, endTime, root.leftChild)
                # return root.leftChild
                return root

        canInsert = [False]
        insert(startTime, endTime, self.root)

        if canInsert[0]:
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

