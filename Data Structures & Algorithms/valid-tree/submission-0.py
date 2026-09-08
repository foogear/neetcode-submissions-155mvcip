class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacentList = {}
        for r, adj in edges:
            if r not in adjacentList:
                adjacentList[r] =   {'root': -1, 'adjacent': []}
            adjacentList[r]['adjacent'].append(adj)

            if adj not in adjacentList:
                adjacentList[adj] = {'root': -1, 'adjacent': []}
            adjacentList[adj]['root'] = r

        def findRoot(adjacentList):
            root = -1 # don't use None because '0'
            for parent in adjacentList:
                #　クソ　None / 0
                if adjacentList[parent]['root'] == -1:
                    print(adjacentList[parent])
                    print(f'rootshouldbe={root}')
                    if root == -1:
                        root = parent
                    else:
                        # tree only one root
                        return -1

            return root

        print(adjacentList)
        print()
        print()
        root = findRoot(adjacentList)
        if root == -1:
            print('no root')
            return False

        def dfs(root):
            visited = set()

            stack = [root]
            while stack:
                parent = stack.pop()
                if parent in visited:
                    # a circle
                    return False
                visited.add(parent)

                for child in adjacentList[parent]['adjacent']:
                    stack.append(child)

            # no multiple root and no circle
            return True
            
        return dfs(root)