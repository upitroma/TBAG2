from GetChoice import getChoice

def Forest(gameState):
    print("You are in the forest.")
    print("What would you like to do?")
    choice = getChoice(["Go to Water front (1)","Go to Large Field (6)","Go to Spider Field (4)","Go to Pond (3)","Save Game"])
    match choice:
        case "Go to Water front (1)":
            gameState.currentLocationID = 1
        case "Go to Large Field (6)":
            gameState.currentLocationID = 6
        case "Go to Spider Field (4)":
            gameState.currentLocationID = 4
        case "Go to Pond (3)":
            gameState.currentLocationID = 3
        case "Save Game":
            gameState.printSaveCode()
            Forest(gameState)
        case _:
            print("Invalid choice")
            Forest(gameState)