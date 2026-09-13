class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])

        # ROW not copied completely, it is same ROW
        # res = [["X"] * COL] * ROW
        # res = []
        # for _ in range(ROW):
        #     res.append(["X"] * COL)

        paintO = set()
        visited = set()
        def bfs(r, c):
            # paint "O"
            stack = [(r, c)]

            while stack:
                print(stack)
                r, c = stack.pop()
                if r < 0 or r >= ROW:
                    continue
                if c < 0 or c >= COL:
                    continue
                if board[r][c] == "X":
                    continue

                if (r, c) in visited:
                    continue
                visited.add((r, c))

                if board[r][c] == "O":
                    print("O")
                    paintO.add((r, c))
                

                stack.append((r - 1, c))
                stack.append((r + 1, c))
                stack.append((    r, c - 1))
                stack.append((    r, c + 1))



        for c in range(COL):
            if board[      0][c] == "O":
                bfs(       0, c)
            if board[ROW - 1][c] == "O":
                bfs( ROW - 1, c)

        for r in range(ROW):
            if board[r][0      ] == "O":
                bfs( r, 0)
            if board[r][COL - 1] == "O":
                bfs( r, COL - 1)

        for r in range(ROW):
            for c in range(COL):
                board[r][c] = "X"
                if (r, c) in paintO:
                    board[r][c] = "O"



