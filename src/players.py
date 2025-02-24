from abc import ABC, abstractmethod
import random

from parse_input import parse_input


class Player(ABC):
    @property
    @abstractmethod
    def character(self):
        pass

    @character.setter
    @abstractmethod
    def character(self, char):
        pass

    @property
    @abstractmethod
    def get_score(self):
        pass

    @abstractmethod
    def increase_score(self):
        pass


class HumanPlayer(Player):
    def __init__(self):
        self._character = None
        self._score = 0

    @property
    def get_score(self):
        """Returns the score of the player."""
        return self._score

    def increase_score(self):
        """Increments the score value by 1."""
        self._score += 1

    @property
    def character(self):
        """Returns the character of the player."""
        return self._character

    @character.setter
    def character(self, char: str):
        """Sets te character of the player.
           Args:
               char (str): The character of the player."""
        self._character = char

    def get_move(self):
        """Gets the move of the player"""
        cell = input("Enter cell where you want to place your move (e.g. A1): ")
        return parse_input(cell)


class ComputerPlayer(Player):
    def __init__(self):
        self._character = None
        self._score = 0

    @property
    def character(self):
        """Returns the character of the bot."""
        return self._character

    @character.setter
    def character(self, char: str):
        """Sets the character of the bot.
           Args:
               char (str): The character of the bot."""
        self._character = char

    @property
    def get_score(self):
        """Returns the score of the bot."""
        return self._score

    def increase_score(self):
        """Increments score value by 1."""
        self._score += 1

    def get_move(self, board):
        """Gets the move of the bot.
           Args:
                board (list): The current board state."""
        is_opponent_winning = self.is_opponent_about_to_win(board)
        if is_opponent_winning[0]:
            return is_opponent_winning[1]
        else:
            rand_col = random.randint(0, 2)
            rand_row = random.randint(0, 2)
            rand_cell = [rand_col, rand_row]
            return rand_cell

    def is_opponent_about_to_win(self, board):
        """Checks if the opponent is about to win.
           Args:
                board (list): The current board state."""
        opponent = 'X' if self._character == 'O' else 'O'
        # Check rows
        for row in board:
            for col in range(3):
                if row[col] == row[col-1] == opponent and row[col-2] == ' ':
                    return [True, [col-2, board.index(row)]]
        # Check columns
        for col in range(3):
            for row in range(3):
                if board[row][col] == board[row-1][col] == opponent and board[row-2][col] == ' ':
                    return [True, [col, row-2]]
        # Check diagonals
        ad = [(0, 2), (1, 1), (2, 0)]  # Anti-diagonals
        for i in range(3):
            if board[i][i] == board[i-1][i-1] == opponent and board[i-2][i-2] == ' ':
                return [True, [i-2, i-2]]
            elif board[ad[i][0]][ad[i][1]] == board[ad[i-1][0]][ad[i-1][1]] == opponent and board[ad[i-2][0]][ad[i-2][1]] == ' ':
                return [True, [ad[i-2][0], ad[i-2][1]]]
            return [False, None]



