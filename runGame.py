from PyUI.Window import Window
from GameScreen import GameScreen
from StartScreen import StartScreen

window = Window("Start Screen", (0,255,0)) ##Create the window to work with

##Create Screen Objects for use------
startScreen = StartScreen(window)
gameScreen = GameScreen(window)
##-----------------------------------

screen = startScreen ##set screen to be the starting screen

while True: ##Game loop
    ##Enter code here to handle changes between screens---
    if screen.state["status"] == "Game Started":
        screen = gameScreen

    ##----------------------------------------------------

    window.checkForInput(screen) #checks for inputs on the screen
    window.update(screen) #updates the window to reflect the new screen