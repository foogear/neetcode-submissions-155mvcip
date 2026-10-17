class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])

        def bfs(curr):
            #print(f'curr{curr}')
            if not curr:
                return 

            next = []
            while curr:
                r, c, currStep = curr.pop()
                #print(f'curr{(r,c)}')
                nextStep = currStep + 1
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
                    if grid[nextR][nextC] > nextStep:
                        grid[nextR][nextC] = nextStep
                        next.append((nextR, nextC, nextStep))
            #print (grid)
            #print(f'next{next}')
            #p#rint()
            bfs(next)


        searchList = []
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    searchList.append((r, c, 0))



        bfs(searchList)