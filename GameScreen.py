import random
from PyUI.Screen import Screen
from PyUI.PageElements import *
from BuiltScreen import *

class GameScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (181,26,58))
        self.state = {
            "status": "Game Started",
            "symbols": ["Amex", "CapitalOne", "chase", "ChaseSlate", "CapitalOneSavor", "Citi", "UsBank", "WellsFargo"]
        }
        self.elements = []

        symbols = self.state["symbols"][:8] * 2
        random.shuffle(symbols)
        random.shuffle(symbols)
        print("Shuffled symbols:", symbols)

        # Create a 4x4 grid of MemoryBox elements
        i = 0
        for x in range(4):
            coordX = 20 * x + 20
            for y in range(4):
                coordY = 20 * y + 20
                hiddenImage = f"./imgus/{symbols[i]}.png"
                self.elements.append(MemoryBox(coordX, coordY, "./imgus/back of card.png", hiddenImage))
                i += 1
