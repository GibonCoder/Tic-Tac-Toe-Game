class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        print(' '*3 + 'A | B | C')
        for index, row in enumerate(self.board):
            print('_'*12)
            print(f'{index+1}. ' + ' | '.join(row))
