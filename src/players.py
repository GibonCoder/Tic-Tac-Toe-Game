from abc import ABC, abstractmethod


class Player(ABC):
    @property
    @abstractmethod
    def character(self):
        pass

    @character.setter
    @abstractmethod
    def character(self, char):
        pass

    @abstractmethod
    def get_move(self):
        pass


class HumanPlayer(Player):
    def __init__(self):
        self._character = None

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, char):
        self._character = char

    def get_move(self):
        cell = input("Enter cell where you want to place your move (e.g. A1): ")
        return cell
