class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not edges: # for block can't address not edges properly 
            if n == 1:
                return True
            else:
                return False

        def findGroup(parent):
            if parent not in group:
                # never use None/0 1️⃣
                return -1

            curr = parent
            updateStack = []
            # while group[parent] != -1: 0️⃣
            while   group[parent] != parent:
                updateStack.append(parent)
                parent = group[parent]

            for vertex in updateStack:
                group[vertex] = parent
                
            return group[curr]

        # parent is GROUP
        group = {}
        groupNum = 0

        for v1, v2 in edges:
            g1 = findGroup(v1)
            g2 = findGroup(v2)
            if g1 == -1 and g2 == -1: # 1️⃣ None/0 NG
                groupNum += 1
                # group[v1] = -1 0️⃣
                group[v1] = v1
                group[v2] = v1
            elif g1 == -1:
                #         = v2
                group[v1] = g2
            elif g2 == -1:
                #         = v1
                group[v2] = g1
            else:
                if g1 == g2:
                    return False # no circle
                else:
                    groupNum -= 1
                    group[g2] = g1

        if groupNum == 1 and len(group) == n:
            return True

        return False