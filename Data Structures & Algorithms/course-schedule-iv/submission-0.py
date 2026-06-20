class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereTree = {c: set() for c in range(numCourses)}
        for p, c in prerequisites:
            prereTree[p].add(c)
        # print(prereTree)

        def findPath(start, end):
            setStack = []
            setStack.append(prereTree[start])

            while setStack:
                for next in setStack.pop():
                    if next == end:
                        return True
                    setStack.append(prereTree[next])

            return False

        res = []
        for p, c in queries:
            res.append(findPath(p, c))

        return res

