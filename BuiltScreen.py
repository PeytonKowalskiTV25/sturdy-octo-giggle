import sys
import pygame
from PyUI.Screen import Screen #will need a screen object to extend
from PyUI.PageElements import * #will need the base element classes to extend
from random import randint

##create the custom screen class
class ExampleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0)) ##use the parents constructor
        ##give the screen a state for updating values and labels----
        self.state = {
            "status": "onGoing",
            "difficulty": "Easy"
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

class EasyDifButton(Button):
    def __init__(self, xCoord, yCoord):
        super().__init__((xCoord, yCoord), 10, 10, "Easy")

    def onClick(self, screen):
        screen.state["difficulty"] = "Easy"
        print("Difficulty set to Easy")
    
class MediumDifButton(Button):
    def __init__(self, xCoord, yCoord):
        super().__init__((xCoord, yCoord), 10, 10, "Medium")
    
    def onClick(self, screen):
        screen.state["difficulty"] = "Medium"
        print("Difficulty set to Medium")

class HardDifButton(Button):
    def __init__(self, xCoord, yCoord):
        super().__init__((xCoord, yCoord), 10, 10, "Hard")

    def onClick(self, screen):
        screen.state["difficulty"] = "Hard"
        print("Difficulty set to Hard")

class MemoryBox(Image):
    def __init__(self, coordX, coordY, imagePath, hiddenImagePath):
        super().__init__(coordX, coordY, 20, 20)
        self.isFlipped = False  # Track if the box is flipped
        self.hiddenImagePath = hiddenImagePath
        self.imagePath = imagePath

    def flip(self):
        self.isFlipped = not self.isFlipped  # Toggle the flipped state
        if self.isFlipped:
            self.imagePath = self.hiddenImagePath  # Change to flipped image
        else:
            self.imagePath = self.imagePath  # Change back to original image