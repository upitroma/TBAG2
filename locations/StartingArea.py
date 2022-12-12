from GetChoice import getChoice


def StartingArea(gameState):
    print("Hello " + gameState.playerName + "!")
    print("You are in the starting area.")
    print("What would you like to do?")
    getChoice(["look around", "go to the forest", "go to the cave", "go to the town", "go to the castle"])
