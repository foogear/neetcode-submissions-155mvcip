class TreeNode:

    def __init__(self, timestamp = -1, value = "", l = None, r = None) -> None:
        self.timestamp = timestamp
        self.value = value
        self.l = l
        self.r = r


class TimeMap:

    def __init__(self):
        self.trees = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        ###print("set")
        if key not in self.trees:
            newTreeName = key
            self.trees[newTreeName] = TreeNode()####

        def insertNode(root, newTimestamp):

            if not root:
                return TreeNode(newTimestamp, value)
            ##print(root.timestamp)

            if newTimestamp > root.timestamp:
                ##print("go r")
                root.r = insertNode(root.r, newTimestamp)
            
            if newTimestamp < root.timestamp:
                ##print("go l")
                root.l = insertNode(root.l, newTimestamp)

            ###print("end set")
            ###print()
            return root

        self.trees[key] = insertNode(self.trees[key], timestamp)

        ####

    def get(self, key: str, timestamp: int) -> str:
        ##print("get")
        if key not in self.trees:
            ###print("")
            return ""

        def find(root, targetTimestamp):
            ##print(root.timestamp)
        

            if   targetTimestamp == root.timestamp:
                ###print("hit")
                return root.value
            elif targetTimestamp  > root.timestamp:
                ###print("go r")
                if not root.r:
                    return root.value
                res = find(root.r, targetTimestamp)
                if not res:
                    return root.value
            else:
                ###print("go l")
                if not root.l:
                    return ""
                res = find(root.l, targetTimestamp)
                if not res:
                    res = root.value

            ##print('end get')
            ##print()
            return res



        return find(self.trees[key], timestamp)
        
