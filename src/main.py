from game import Game
from players import HumanPlayer, ComputerPlayer

game = Game()
human = HumanPlayer()
human.character = 'X'
computer = ComputerPlayer()
computer.character = 'O'

while True:
    game.print_board()
    move = human.get_move()
    if game.place_move(move, human.character):
        is_win = game.check_win()
        if is_win[0]:
            game.print_board()
            print(f'Game over! {is_win[1]} wins!')
            break
        elif game.is_tie():
            game.print_board()
            print('It\'s a tie!')
            break
        move = computer.get_move(game.board)
        game.place_move(move, computer.character)
        is_win = game.check_win()
        if is_win[0]:
            game.print_board()
            print(f'Game over! {is_win[1]} wins!')
            break
        elif game.is_tie():
            game.print_board()
            print('It\'s a tie!')
            break
