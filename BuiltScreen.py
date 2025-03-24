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

class MemoryBox(Button):
    def __init__(self, coordX, coordY, imagePath, hiddenImagePath):
        super().__init__((coordX, coordY), 20, 20, "")
        self.imagePath = imagePath
        self.hiddenImagePath = hiddenImagePath
        self.hidden = True  # Initially hidden
        self.currentImage = imagePath
        self.rect = pygame.Rect(coordX, coordY, 20, 20)  # Define the rect attribute

    def toggleVisibility(self):
        self.hidden = not self.hidden
        self.currentImage = self.imagePath if not self.hidden else self.hiddenImagePath

    def display(self, surface):
        # Draw the current image
        img = pygame.image.load(self.currentImage)
        img = pygame.transform.scale(img, (self.rect[2], self.rect[3]))
        surface.blit(img, (self.rect[0], self.rect[1]))

    def onClick(self, screen):
        self.toggleVisibility()
        print(f"Box at {self.position} clicked, hidden: {self.hidden}, currentImage: {self.currentImage}")