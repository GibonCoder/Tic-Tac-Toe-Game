from game import Game
from players import HumanPlayer, ComputerPlayer
from assign_symbols import assign_symbols

game = Game()
human = HumanPlayer()
computer = ComputerPlayer()

human.character, computer.character = assign_symbols()

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
        while not game.place_move(move, computer.character):
            if game.is_board_full():
                break
            move = computer.get_move(game.board)
        is_win = game.check_win()
        if is_win[0]:
            game.print_board()
            print(f'Game over! {is_win[1]} wins!')
            break
        elif game.is_tie():
            game.print_board()
            print('It\'s a tie!')
            break
        elif game.is_board_full():
            game.print_board()
            print('Board is full. It\'s a tie!')
            break
