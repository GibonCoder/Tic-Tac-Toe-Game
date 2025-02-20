from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def get_move(self):
        pass


class HumanPlayer(Player):
    def get_move(self):
        cell = input("Enter cell where you want to place your move (e.g. A1): ")
        return cell
