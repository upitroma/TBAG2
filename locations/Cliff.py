from GetChoice import getChoice

def Cliff(gameState):
    print("You are at the cliff.")
    print("What would you like to do?")
    choice = getChoice(["Go to Waterfall (7)","Go to Dunes (5)","Go to Abyss Entrance (9)","Save Game"])
    match choice:
        case "Go to Waterfall (7)":
            gameState.currentLocationID = 7
        case "Go to Dunes (5)":
            gameState.currentLocationID = 5
        case "Go to Abyss Entrance (9)":
            gameState.currentLocationID = 9
        case "Save Game":
            gameState.printSaveCode()
            Cliff(gameState)
        case _:
            print("Invalid choice")
            Cliff(gameState)