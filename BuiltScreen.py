import sys
import pygame
from PyUI.Screen import Screen
from PyUI.PageElements import *

##create the custom screen class
class ExampleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0)) ##use the parents constructor
        ##give the screen a state for updating values and labels----
        self.state = {
            "status": "onGoing"
        }
        ##----------------------------------------------------------

    def elementsToDisplay(self): #defines what elements will be on the page
        self.elements = [
            Label((300, 200), 100, 100, self.state["status"], 14, (255,255,255))
        ]
        
##Add custom page elements
class StartButton(Button):
    def __init__(self, xCoord, yCoord):
        super().__init__((xCoord, yCoord), 10, 10, "Start")
    
    def onClick(self, screen):
        screen.state["status"] = "Game Started"

class QuitButton(Button):
    def __init__(self, xCoord, yCoord):
        super().__init__((xCoord, yCoord), 10, 10, "Quit")

    def onClick(self, screen):
        print("Quit button clicked")  # Debugging statement
        pygame.quit()
        sys.exit()

class MemoryBox(Image):
    def __init__(self, coordX, coordY, coverImagePath, hiddenImagePath):
        self.coverImagePath = coverImagePath
        self.hiddenImagePath = hiddenImagePath
        self.hidden = True
        super().__init__((coordX, coordY), 15, 15, self.coverImagePath)
        
    def onClick(self, screen):
        if self.hidden == True:
            self.imagePath = self.hiddenImagePath
            self.hidden = False
            screen.state["shownCards"] += 1