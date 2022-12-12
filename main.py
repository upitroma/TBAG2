from GameState import GameState
from GetChoice import getChoice
from locations.StartingArea import StartingArea

areas = ["StartingArea", "Forest", "Cave", "Town", "Castle"]

def createCharacter():
    print("What is your name? (no more than 10 characters)")
    playerName = input()
    if len(playerName) > 10:
        print("Name too long")
        createCharacter()
    else:
        return playerName

def loadLevel(gameState):
    match areas[gameState.currentLocationID]:
        case "StartingArea":
            StartingArea(gameState)
        case _:
            print("You are in an unknown area.")
        # case "Forest":
        #     Forest(gameState)
        # case "Cave":
        #     Cave(gameState)
        # case "Town":
        #     Town(gameState)
        # case "Castle":
        #     Castle(gameState)


def titleScreen():
    print("Welcome!\n")
    match getChoice(["New Game", "Continue Game"]):
        case "New Game":
            gameState = GameState()
            gameState.printSaveCode()
            print("You can return to your game at any time by entering this code on the title screen.")
            print("I'll send you back to the title screen now. Give it a try!")
            print()
            titleScreen()
        case "Continue Game":
            print("Enter your save code:")
            saveCode = input()
            gameState = GameState(saveCode)
            if gameState.validGameState:
                loadLevel(gameState)
            else:
                print("Invalid save code")
                print()
                titleScreen()
titleScreen()