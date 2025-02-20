class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        """Prints the current state of the board."""

        print(' '*3 + 'A | B | C')
        for index, row in enumerate(self.board):
            print('_'*12)
            print(f'{index+1}. ' + ' | '.join(row))

    def place_move(self, cell: list, player: str):
        """Places a move on the board.
           Args:
               cell (list): The cell to place the move.
               player (str): The player making the move."""
        if self.validate_move(cell):
            self.board[cell[1]][cell[0]] = player
        else:
            raise ValueError('Invalid move!')

    def validate_move(self, cell: list):
        """Checks if a move is valid.
           Args:
               cell (list): The cell to validate."""
        if cell[1] < 1 or cell[1] > 3:
            return False
        elif self.board[cell[1]][cell[0]] != ' ':
            return False
        return True

    def check_win(self):
        """Checks if one of players has won the game."""
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
        # Check columns
        for column in range(3):
            if self.board[0][column] == self.board[1][column] == self.board[2][column] != ' ':
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_tie(self):
        """Checks if the game is a tie."""
        return all(cell != ' ' for row in self.board for cell in row) and self.check_win() is False
