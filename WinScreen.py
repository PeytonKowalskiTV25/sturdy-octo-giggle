from PyUI.Screen import Screen
from PyUI.PageElements import *
from BuiltScreen import *

class WinScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (181,26,58))
        self.state = {
            "status": "Game Won"
        }
    
    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((300, 200), 100, 100, "You Won! Your'e now in mass credit card debt.", 14, (0,0,0)), #dynamic element needs arguments
            StartButton(40, 50),
            QuitButton(60, 50)
        ]