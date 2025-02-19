from transform_column import transform_column


class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        print(' '*3 + 'A | B | C')
        for index, row in enumerate(self.board):
            print('_'*12)
            print(f'{index+1}. ' + ' | '.join(row))

    def place_move(self, row, col, player):
        transformed_col = transform_column(col)
        if self.validate_move(row, transformed_col):
            self.board[row-1][transformed_col] = player
        else:
            raise ValueError('Invalid move!')

    def validate_move(self, row, col):
        if row < 1 or row > 3:
            return False
        elif self.board[row-1][col] != ' ':
            return False
        return True

    def check_win(self):
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
        return all(cell != ' ' for row in self.board for cell in row) and self.check_win() is False
