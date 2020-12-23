'''
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''
class Solution:
    
    def solveNQueens(self, rows: int):
        results = []
        puzzle = []
        diagonal = set()
        antidiagonal = set()
        cols = set()

        def do_solve(row = 0):
            if row == rows:
                results.append(puzzle[:])
                return

            for col in range(rows):
                if col in cols or (row + col) in diagonal or (row - col) in antidiagonal: continue

                puzzle.append("." * col + "Q" + "." * (rows - col - 1))
                cols.add(col)
                diagonal.add(row + col)
                antidiagonal.add(row - col)

                do_solve(row + 1)

                cols.remove(col)
                diagonal.remove(row + col)
                antidiagonal.remove(row - col)
                puzzle.pop()

        do_solve()
        return results

print(Solution().solveNQueens(4))