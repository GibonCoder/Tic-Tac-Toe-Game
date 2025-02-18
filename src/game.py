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
        self.board[row-1][transformed_col] = player

    def validate_move(self, row, col):
        if row < 1 or row > 3:
            return False
        elif self.board[row-1][col] != ' ':
            return False
        return True
