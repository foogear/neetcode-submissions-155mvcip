import queue

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])

        def bfs(r, c):
            # searchQueue = queue.Queue()
            # searchQueue.put((r, c))
            searchQueue = deque()
            searchQueue.append((r, c))

            step = 0
            while searchQueue:


                step += 1
                # numLayerNode = searchQueue.qsize()
                numLayerNode = len(searchQueue)
                #print(searchQueue)
                for _ in range(numLayerNode):
                    # r, c = searchQueue.get()
                    r, c = searchQueue.popleft()
                    
                    up    = (r - 1, c)
                    down  = (r + 1, c)
                    left  = (    r, c - 1)
                    right = (    r, c + 1)
                    direction = (up, down, left, right)
                    for nextR, nextC in direction:
                        if nextR < 0 or nextR >= ROW:
                            continue
                        if nextC < 0 or nextC >= COL:
                            continue
                        if  grid[nextR][nextC] > step:
                            grid[nextR][nextC] = step
                            # searchQueue.put((nextR, nextC))
                            searchQueue.append((nextR, nextC))
                    
                





        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    #print((r, c))
                    bfs(r, c)

                    #for R in grid:
                       # print(R)