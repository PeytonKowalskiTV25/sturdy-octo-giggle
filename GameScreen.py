import random
from PyUI.Screen import Screen
from PyUI.PageElements import *
from BuiltScreen import *

class GameScreen(Screen):
    def __init__(self, window, difficulty):
        super().__init__(window, (181,26,58))
        self.state = {
            "status": "Game Started",
            "difficulty": difficulty,
            "symbols": ["Amex", "CapitalOne", "chase", "ChaseSlate", "CapitalOneSavor", "Citi", "UsBank", "WellsFargo"]
        }

    def elementsToDisplay(self):
        self.elements = []
        boardSize = 4
        symbols = []

        if self.state["difficulty"] == "Easy":
            symbols = self.state["symbols"][:4] * 2  # Two of each of the first 4 symbols
        elif self.state["difficulty"] == "Medium":
            boardSize = 6
            symbols = self.state["symbols"][:6] * 2  # Two of each of the first 6 symbols
        elif self.state["difficulty"] == "Hard":
            boardSize = 8
            symbols = self.state["symbols"][:8] * 2  # Two of each of the first 8 symbols

        random.shuffle(symbols)  # Shuffle the symbols

        index = 0
        for x in range(boardSize):
            coordX = 40 * x + 25
            for y in range(boardSize):
                if index >= len(symbols):
                    break
                coordY = 20 * y + 20
                hiddenImage = f"./imgus/{symbols[index]}.png"
                self.elements.append(MemoryBox(coordX, coordY, "./imgus/back of card.png", hiddenImage))
                index += 1