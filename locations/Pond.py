from GetChoice import getChoice

def Pond(gameState):
    print("You are at the pond.")
    print("What would you like to do?")
    choice = getChoice(["Go to forest (2)","Go to Waterfall (7)","Save Game"])
    match choice:
        case "Go to forest (2)":
            gameState.currentLocationID = 2
        case "Go to Waterfall (7)":
            gameState.currentLocationID = 7
        case "Save Game":
            gameState.printSaveCode()
            Pond(gameState)
        case _:
            print("Invalid choice")
            Pond(gameState)