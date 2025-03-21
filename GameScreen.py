from PyUI.Screen import Screen
from PyUI.PageElements import *
from BuiltScreen import *

class GameScreen(Screen):
    def __init__(self, window, difficulty):
        super().__init__(window, (181,26,58))
        self.state = {
            "status": "Game Started",
            "difficulty": difficulty
        }

    def elementsToDisplay(self):
        self.elements = []
        boardSize = 4
        if self.state["difficulty"] == "Medium":
            boardSize = 6
        elif self.state["difficulty"] == "Hard":
            boardSize = 8

        for x in range(boardSize):
            for y in range(4):
                coordX = 20*x + 20
                coordY = 20*y + 20
                self.elements.append(MemoryBox(coordX, coordY, "./imgus/Allen.jpg", "./imgus/Mark.jpg"))