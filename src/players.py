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
        """Gets the move of the bot."""
        rand_col = random.randint(0, 2)
        rand_row = random.randint(0, 2)
        rand_cell = [rand_col, rand_row]

        return rand_cell
