from game import Game
from players import HumanPlayer, ComputerPlayer

game = Game()
human = HumanPlayer()
human.character('X')
computer = ComputerPlayer()
computer.character('O')

for _ in range(5):
    game.print_board()
    move = human.get_move()
    game.place_move(move, human.character)
    game.print_board()
    move = computer.get_move()
    game.place_move(move, computer.character)
    game.print_board()
    if game.check_win():
        print('Game over!')
        break
    elif game.is_tie():
        print('It\'s a tie!')
        break