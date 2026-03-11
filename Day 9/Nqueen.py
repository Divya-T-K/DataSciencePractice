class Solution(object):
    def solveNQueens(self, n):
        r = []
        b = [["."] * n for _ in range(n)]

        l = [0] * n
        up = [0] * (2*n - 1)
        lo = [0] * (2*n - 1)

        self.solve(0, r, b, l, up, lo)
        return r

    def solve(self, c, r, b, l, up, lo):
        n = len(b)

        if c == n:
            temp = []
            for i in range(n):
                temp.append("".join(b[i]))
            r.append(temp)
            return

        for i in range(n):
            if l[i] == 0 and up[n-1 + c - i] == 0 and lo[c + i] == 0:

                b[i][c] = "Q"
                l[i] = 1
                up[n-1 + c - i] = 1
                lo[c + i] = 1

                self.solve(c + 1, r, b, l, up, lo)

                b[i][c] = "."
                l[i] = 0
                up[n-1 + c - i] = 0
                lo[c + i] = 0