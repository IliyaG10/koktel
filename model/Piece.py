from abc import ABC, abstractmethod

class Piece(ABC):

    @abstractmethod
    def move(self, board, position):
        pass


    @abstractmethod
    def attack(self, board, position):
        pass