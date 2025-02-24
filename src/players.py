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
        # Check rows and columns
        for i in range(3):
            # Check rows
            if board[i].count(opponent) == 2 and ' ' in board[i]:
                return [True, [board[i].index(' '), i]]
            # Check columns
            column = [board[j][i] for j in range(3)]
            if column.count(opponent) == 2 and ' ' in column:
                return [True, [i, column.index(' ')]]
        # Check main diagonal
        diag = [board[i][i] for i in range(3)]
        if diag.count(opponent) == 2 and ' ' in diag:
            empty_index = diag.index(' ')
            return [True, [empty_index, empty_index]]
        # Check anti-diagonal
        anti_diag = [board[i][2-i] for i in range(3)]
        if anti_diag.count(opponent) == 2 and ' ' in anti_diag:
            empty_index = anti_diag.index(' ')
            return [True, [2-empty_index, empty_index]]
        return [False, None]
