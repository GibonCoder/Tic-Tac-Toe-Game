from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def get_move(self):
        pass


class HumanPlayer(Player):
    def __init__(self):
        self._character = None

    def get_character(self):
        return self._character

    def set_character(self, char):
        self._character = char

    def get_move(self):
        cell = input("Enter cell where you want to place your move (e.g. A1): ")
        return cell


