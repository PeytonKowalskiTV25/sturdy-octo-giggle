from PyUI.Screen import Screen
from BuiltScreen import *
from PyUI.PageElements import Label

class StartScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (181,26,58))
        self.state = {
            "status": "Welcome",
            "difficulty": "Easy"
        }
        self.difficulties = ["Easy", "Medium", "Hard"]
        self.currentIndex = 0

    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((300, 200), 100, 100, self.state["status"], 14, (0,0,0)), #dynamic element needs arguments
            StartButton(40, 10),
            QuitButton(60, 10),
            EasyDifButton(35, 40),
            MediumDifButton(50, 40),
            HardDifButton(65, 40),
            Label((50, 80), 100, 100, self.difficulties[self.currentIndex], 14, (0,0,0)) #display current difficulty level
        ]