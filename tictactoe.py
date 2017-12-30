# Board is represented by 2-D array
class Board(object):

    def __init__(self, size=3):
        self.size = size
        self.player = 0
        self.turns = 0
        self.rows = [(0,0) for i in xrange(size)]
        self.cols = [(0,0) for i in xrange(size)]
        self.diag = (0,0)
        self.antiDiag = (0,0)
        self.board = [[' ' for i in xrange(size)] for i in xrange(size)]

    def place(self,x,y):
        if self.board[y][x] != ' ':
            return "Invalid move"

        if player == 0:
            self.board[y][x] = 'X'
        elif player == 1:
            self.board[y][x] = 'Y'

        self.rows[y][player] += 1
        self.cols[x][player] += 1

        # diagonal
        if (x == y):
            self.diag[player] += 1

        # anti diagonal
        if (x + y == 2):
            self.antiDiag[player] += 1

        self.__changePlayer()

        return "Player " + self.player + " turn"

    def checkWin(self):
        if self.turns == self.size:
            return "Tied Game"

        if self.diag[0] == self.size or self.antiDiag[0] == self.size:
            return "Player 0 Win"
        if self.diag[1] == self.size or self.antiDiag[1] == self.size:
            return "Player 1 Win"

        for row in self.rows:
            if row[0] == self.size:
                return "Player 0 Win"
            if row[1] == self.size:
                return "Player 1 Win"

        for col in self.cols:
            if col[0] == self.size:
                return "Player 0 Win"
            if col[1] == self.size:
                return "Player 1 Win"

        return None

    def draw(self):
        for row in self.board[0]:
            for pos in row:
                print("| " + pos)
            print("  |\n")

    def __changePlayer(self):
        self.player = self.player ^ 1

if __name__ == '__main__':
    game = Board()
    game.draw()
