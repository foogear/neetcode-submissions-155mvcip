class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        groupRoot = {}
        groupMap = {}

        def findRoot(x):
            xp = x
            while xp != groupMap[xp]:
                xp = groupMap[xp]
                groupMap[x] = xp
            return xp

        for account in accounts:
            root = None
            a = account[1]
            if (a not in groupRoot and
                a not in groupMap):
                groupRoot[a] = account[0]
                root = a
            for i in range(1, len(account)):
                a = account[i]
                if a in groupMap:
                    newRoot = findRoot(a)
                    groupMap[root] = newRoot
                    del groupRoot[root]
                    root = newRoot
                    continue
                groupMap[a] = root
                
        def createList(groupRoot, groupMap):
            print(groupRoot)
            print(groupMap)

            res = []
            rootIndex = {}
            index = 0
            for a in groupMap:
                root = findRoot(a)
                if root not in rootIndex:
                    res.append([])
                    res[index].append(groupRoot[root])
                    rootIndex[root] = index
                    index += 1
                res[rootIndex[root]].append(a)

            return res

        return createList(groupRoot, groupMap)

