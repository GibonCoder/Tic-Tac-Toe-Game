from game import Game
from players import HumanPlayer, ComputerPlayer

game = Game()
human = HumanPlayer()
human.character = 'X'
computer = ComputerPlayer()
computer.character = 'O'

for _ in range(5):
    game.print_board()
    move = human.get_move()
    while game.validate_move(move):
        move = human.get_move()
    game.place_move(move, human.character)
    game.print_board()
    move = computer.get_move(game.board)
    # TODO: FIX 1
    while game.validate_move(move):
        move = computer.get_move(game.board)
    game.place_move(move, computer.character)
    if game.check_win():
        print('Game over!')
        break
    elif game.is_tie():
        print('It\'s a tie!')
        break
