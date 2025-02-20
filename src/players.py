from abc import ABC, abstractmethod


class Player(ABC):
    @property
    @abstractmethod
    def score(self):
        pass

    @abstractmethod
    def increase_score(self):
        pass

    @abstractmethod
    def get_move(self):
        pass


class HumanPlayer(Player):
    def __init__(self):
        self._character = None
        self._score = 0

    @property
    def score(self):
        return self._score

    def increase_score(self):
        self._score += 1

    def get_character(self):
        return self._character

    def set_character(self, char):
        self._character = char

    def get_move(self):
        cell = input("Enter cell where you want to place your move (e.g. A1): ")
        return cell


