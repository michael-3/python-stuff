
# Return all distinct nxn configurations such that n queens do not conflict
def nQueens(n):
    solutions = []
    def dfs(queens, xy_sum, xy_diff):
        p = len(queens)
        if p == n:
            solutions.append(queens)
            return
        for q in xrange(n):
            if q not in queens and p - q not in xy_diff and p + q not in xy_sum:
                dfs(queens+[q], xy_sum+[p+q], xy_diff+[p-q])
    dfs([],[],[])
    return queens

# Assume board - 2D array
def isSafe(board, x, y):
    # row-wise check

    # col-wise check

    # diagonal check

    # anti-diagonal check

def nQueens2(n):
    board = [[0 for i in xrange(n)] for i in xrange(n)]
