class Solution(object):
    def solveSudoku(self, board):
        rows = [0]*9
        cols = [0]*9
        boxes = [0]*9
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    num = int(board[i][j]) - 1
                    mask = 1 << num
                    rows[i] |= mask
                    cols[j] |= mask
                    boxes[(i//3)*3 + j//3] |= mask

        def backtrack(k):
            if k == len(empty):
                return True

            i, j = empty[k]
            box = (i//3)*3 + j//3

            for num in range(9):
                mask = 1 << num
                if rows[i] & mask or cols[j] & mask or boxes[box] & mask:
                    continue

                board[i][j] = str(num+1)
                rows[i] |= mask
                cols[j] |= mask
                boxes[box] |= mask

                if backtrack(k+1):
                    return True

                board[i][j] = "."
                rows[i] ^= mask
                cols[j] ^= mask
                boxes[box] ^= mask

            return False

        backtrack(0)