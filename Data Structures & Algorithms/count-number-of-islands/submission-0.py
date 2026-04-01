class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
                                    #Its str NOT int !!!!!
        explored = {}
        count = 0

        def dfs(grid, r, c, explored):

            grid[r][c] = "0"
            explored[(r, c)] = True

            goUp =   r - 1 >= 0
            goDown = r + 1 <= len(grid) - 1
            goLeft = c - 1 >= 0
            goRight = len(grid) > 0 and c + 1 <= len(grid[0]) - 1

            if goUp:
                if       grid[r - 1][c] == "0":
                    explored[(r - 1, c)] = True
                else:
                    dfs(grid, r - 1, c, explored)
            if goDown:
                if       grid[r + 1][c] == "0":
                    explored[(r + 1, c)] = True
                else:
                    dfs(grid, r + 1, c, explored)
            if goLeft:
                if       grid[r][c - 1] == "0":
                    explored[(r, c - 1)] = True
                else:
                    dfs(grid, r, c - 1, explored)
            if goRight:
                if       grid[r][c + 1] == "0":
                    explored[(r, c + 1)] = True
                else:
                    dfs(grid, r, c + 1, explored)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ##print("------------")
                ##print(f"{r},{c}")
                ##print(explored.keys())
                pointToExplore = (r, c)
                if pointToExplore not in explored:
                    if grid[r][c] == "0":
                        explored[(r, c)] = True
                    else:
                        count += 1
                        print("DFS")
                        dfs(grid, r, c, explored)

        return count