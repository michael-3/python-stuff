# Given board is a 9 x 9 sudoku board represented by a 2D array
def isValid(board):
    # assume n x n board
    size = len(board)
    # check all rows
    for row in board:
        used = {}
        for number in row:
            if number != '.':
                if used.contains(number):
                    return False
                else:
                    used[number] = True

    # check all columns
    for col in xrange(size):
        used = {}
        for row in xrange(size):
            number = board[row][col]
            if number != '.':
                if used.contains(number):
                    return False
                else:
                    used[number] = True

    # check all 3x3 grids
    for n in xrange(size):
        used = {}
        for i in xrange(n/3*3,n/3*3+3,1):
            for j in xrange(n%3*3,n%3*3+3,1):
                number = board[i][j]
                if number != '.':
                    if used.contains(number):
                        return False
                    else:
                        used[number] = True

# cleaner method is to abstract out a isDuplicate function that checks whether
# duplicates exists in the board between start-end row and start-end column
def isValid2(board):
     size = len(board)
    # row check
    if hasDuplicate(board, 0, size, 0, size):
        return False
    # col check
    for i in xrange(size):
        if hasDuplicate(board, i, i, 0, size):
            return False
    # 3x3 grids
    grid = sqrt(size)
    for i in xrange(grid):
        for k in xrange(grid):
            if hasDuplicated(board, i*grid, i*grid+grid-1, k*grid, k*grid+grid-1):
                return False

    return True

def hasDuplicate(board, row_start, row_end, col_start, col_end):
    used = {}
    for row in xrange(row_start, row_end+1, 1):
        for col in xrange(col_start, col_end+1, 1):
            if board[row][col] != '.':
                if used.contains(board[row][col]):
                    return True
                else:
                    used[board[row][col]] = 1
    return False
