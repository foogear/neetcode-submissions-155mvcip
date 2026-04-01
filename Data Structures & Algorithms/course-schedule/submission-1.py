class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prerequisitesMap = {}

        for p in prerequisites:
            if p[0] not in prerequisitesMap:
                prerequisitesMap[p[0]] = {"child": [], "hasParent": False}
            prerequisitesMap[p[0]]["child"].append(p[1])
            if p[1] not in prerequisitesMap:
                prerequisitesMap[p[1]] = {"child": [], "hasParent": False}
            prerequisitesMap[p[1]]["hasParent"] = True

        for p in prerequisitesMap:
            print(p, end = "")
            print(prerequisitesMap[p])

        # They will give me MORE than one tree so root is useless
        # def search(root, prerequisitesMap)
        def search(prerequisitesMap):

            visited = set()

            for p in prerequisitesMap:

                queue = collections.deque()
                treeNode = set()
                queue.append(p) 

                while queue:
                    node = queue.popleft()

                    # if node in treeNode: -Err 1
                    #    return False -Err 1
                    treeNode.add(node)
                    visited.add(node)
                    
                    for child in prerequisitesMap[node]["child"]:
                        # check BEFORE add -Err 1
                        if child in treeNode:
                            return False
                        if child not in visited:
                            queue.append(child)
            


            return True

        return search(prerequisitesMap)


