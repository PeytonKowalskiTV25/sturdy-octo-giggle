import random
from PyUI.Screen import Screen
from PyUI.PageElements import *
from BuiltScreen import *

class GameScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (181,26,58))
        self.state = {
            "status": "Game Started",
            "symbols": ["Amex", "CapitalOne", "chase", "ChaseSlate", "CapitalOneSavor", "Citi", "UsBank", "WellsFargo"],
            "shownCards" : 0
        }
        self.matches = 0
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
        
    def checkPairs(self):
        revealedElements = []
        for element in self.elements:
            if not element.hidden:
                revealedElements.append(element)

        if self.state["shownCards"] == 2:
            if revealedElements[0].hiddenImagePath == revealedElements[1].hiddenImagePath:
                print("It's a match!")
                for element in revealedElements:
                    self.elements.remove(element)
                    self.matches += 1
            else:
                print("Not a match!")
        for element in revealedElements:
            element.hidden = True
            element.imagePath = element.coverImagePath
            self.state["shownCards"] = 0
