from PyUI.Window import Window
from GameScreen import GameScreen
from StartScreen import StartScreen
from time import sleep

window = Window("Start Screen", (0,255,0))
window2 = Window("Game Screen", (0,255,0))

##Create Screen Objects for use------
startScreen = StartScreen(window)
gameScreen = GameScreen(window2)
##-----------------------------------

screen = startScreen

while True: ##Game loop
    ##Enter code here to handle changes between screens---
    if screen.state["status"] == "Game Started":
        screen = gameScreen

        if screen.state["shownCards"] >= 2:
            screen.checkPairs()
            sleep(2)
            if screen.elements == []:
                print("You Won!!")
                screen = startScreen
    ##----------------------------------------------------

    window.checkForInput(screen) #checks for inputs on the screen
    window.update(screen) #updates the window to reflect the new screen