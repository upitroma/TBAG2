from GetChoice import getChoice

def Dunes(gameState):
    print("You are in the dunes.")
    print("What would you like to do?")
    choice = getChoice(["Go to Large Field (6)","Go to Spider Field (4)","Go to Cliff (8)","Save Game"])
    match choice:
        case "Go to Large Field (6)":
            gameState.currentLocationID = 6
        case "Go to Spider Field (4)":
            gameState.currentLocationID = 4
        case "Go to Cliff (8)":
            gameState.currentLocationID = 8
        case "Save Game":
            gameState.printSaveCode()
            Dunes(gameState)
        case _:
            print("Invalid choice")
            Dunes(gameState)