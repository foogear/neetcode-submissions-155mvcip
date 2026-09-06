class Solution:
    def exist(self, board: List[List[str]], target: str) -> bool:
        sameCell = set()
        targetLen = len(target)
        def search(r, c, i):
            if i == targetLen: # i should do this first
                return True

            if r < 0 or r >= len(board):
                return False
            if c < 0 or c >= len(board[0]):
                return False

            if (r, c) in sameCell:
                return False

            if board[r][c] != target[i]:
                return False

            sameCell.add((r, c))

            nextTarget = i + 1
            up    = search(r - 1,     c, nextTarget)
            down  = search(r + 1,     c, nextTarget)
            left  = search(    r, c - 1, nextTarget)
            right = search(    r, c + 1, nextTarget)

            if not (up or down or left or right):
                sameCell.remove((r, c))
                return False

            return True

        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c] == target[0]:
                    if search(r, c, 0):
                        return True

        return False