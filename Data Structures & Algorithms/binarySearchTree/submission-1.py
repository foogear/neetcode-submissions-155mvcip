class TreeNode:
    
    def __init__(self, key, val, left=None, right=None):
        self.key   = key
        self.val   = val
        self.left  = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = TreeNode('ROOT',0)
        
    def insert(self, key: int, val: int) -> None:
        if not self.root.left:
            self.root.left = TreeNode(key, val)
            return 
        
        targetNode = self.root.left
        while True:
            if   key < targetNode.key and targetNode.left:
                targetNode = targetNode.left
                continue 
            elif key > targetNode.key and targetNode.right:
                targetNode = targetNode.right
                continue 
            elif key == targetNode.key:
                targetNode.val = val
            break 
            
        if key < targetNode.key:
            targetNode.left  = TreeNode(key, val)
        else:
            targetNode.right = TreeNode(key, val)
        return
    
    def get(self, key: int) -> int:
        if not self.root.left:
            return -1
            
        targetNode = self.root.left
        while targetNode:
            if   key < targetNode.key:
                targetNode = targetNode.left
            elif key > targetNode.key:
                targetNode = targetNode.right
            else:
                return targetNode.val
        return -1
        
    def getMin(self) -> int:
        if not self.root.left:
            return -1
            
        targetNode = self.root.left
        while targetNode.left:
            targetNode = targetNode.left
        
        return targetNode.val
        
    def getMax(self) -> int:
        if not self.root.left:
            return -1
            
        targetNode = self.root.left
        while targetNode.right:
            targetNode = targetNode.right
        
        return targetNode.val

    def buildKeysList(self, root) -> List[int]:
        if not root:
            return []

        keysList = []
        if root.left:
            keysList += self.buildKeysList(root.left)
        keysList += [root.key]
        if root.right:
            keysList += self.buildKeysList(root.right)

        return keysList

    def getInorderKeys(self) -> List[int]:
        return self.buildKeysList(self.root.left)

    def removeNode(self, root, key: int):
        
        # special return
        if not root:
            return
        if 'ROOT' == root.key:
            root.left = self.removeNode(root.left, key)
            return root
        if    key == root.key:
            if root.left and root.right:
                leftMaxNode = root.left
                while leftMaxNode.right:
                    leftMaxNode = leftMaxNode.right
                leftMaxNode.right = root.right
                return root.left
            elif root.left:
                return root.left
            else:
                return root.right
        
        # recursive search
        if   key < root.key:
            root.left  = self.removeNode(root.left,  key)
        elif key > root.key:
            root.right = self.removeNode(root.right, key)
        return root
        
    def remove(self, key: int) -> None:
        self.root = self.removeNode(self.root, key)
        return


