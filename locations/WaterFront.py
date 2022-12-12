from GetChoice import getChoice

def WaterFront(gameState):
    print("You are in the water front.")
    print("What would you like to do?")
    choice = getChoice(["Go to Base Camp","Go to Large Field (6)","Go to Forest (2)","Save Game"])
    match choice:
        case "Go to Base Camp":
            gameState.currentLocationID = 0
        case "Go to Large Field (6)":
            gameState.currentLocationID = 6
        case "Go to Forest (2)":
            gameState.currentLocationID = 2
        case "Save Game":
            gameState.printSaveCode()
            WaterFront(gameState)
        case _:
            print("Invalid choice")
            WaterFront(gameState)

