class TreeNode:

    def __init__(self, timestamp = -1, value = None, l = None, r = None) -> None:
        self.timestamp = timestamp
        self.value = value
        self.l = l
        self.r = r


class TimeMap:

    def __init__(self):
        self.trees = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.trees:
            newTreeName = key
            self.trees[newTreeName] = TreeNode()####

        def insertNode(root, newTimestamp):
            if not root:
                return TreeNode(newTimestamp, value)

            if newTimestamp > root.timestamp:
                root.r = insertNode(root.r, newTimestamp)
            
            if newTimestamp < root.timestamp:
                root.l = insertNode(root.l, newTimestamp)

            return root

        self.trees[key] = insertNode(self.trees[key], timestamp)

        ####

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.trees:
            return ""

        def find(root, targetTimestamp):
        

            if   targetTimestamp == root.timestamp:
                return root.value
            elif targetTimestamp  > root.timestamp:
                if not root.r:
                    return root.value
                res = find(root.r, targetTimestamp)
            else:
                if not root.l:
                    return ""
                res = find(root.l, targetTimestamp)

            return res



        return find(self.trees[key], timestamp)
        
