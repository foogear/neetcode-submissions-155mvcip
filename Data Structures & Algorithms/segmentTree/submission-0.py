class SegmentTree:
    
    def __init__(self, nums: List[int]):
        # 関数ごと五行ぐらい　小さく分ける
        def createTree(leftBound, rightBound):
            if leftBound == rightBound:
                return TreeNode(nums[leftBound], None, None, leftBound, rightBound)

            m = (leftBound + rightBound) // 2
            leftChild  = createTree(leftBound, m)
            rightChild = createTree(m + 1, rightBound)
            sum = leftChild.sum + rightChild.sum
            root = TreeNode(sum, leftChild, rightChild, leftBound, rightBound)

            return root
        
        self.root = createTree(0, len(nums) - 1)

    def update(self, index: int, val: int, root = None) -> None:
        if not root:
            root = self.root
        if root.leftBound == root.rightBound:
            root.sum = val
            return 

        m = (root.leftBound + root.rightBound) // 2
        if index > m:
            self.update(index, val, root.rightChild)
        else:
            self.update(index, val, root.leftChild)

        root.sum = root.leftChild.sum + root.rightChild.sum

    def query(self, L: int, R: int, root = None) -> int:
        if not root:
            root = self.root
        if L == root.leftBound and R == root.rightBound:
            return root.sum

        m = (root.leftBound + root.rightBound) // 2
        if L > m:
            return self.query(L, R, root.rightChild)
        elif R <= m:
            return self.query(L, R, root.leftChild)
        else:
            return (self.query(L,     m, root.leftChild) +
                    self.query(m + 1, R, root.rightChild))

class TreeNode:
    def __init__(self, s, lc, rc, lb, rb) -> None:
        self.sum = s
        self.leftChild = lc
        self.rightChild = rc
        self.leftBound  = lb
        self.rightBound = rb