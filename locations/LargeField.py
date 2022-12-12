from GetChoice import getChoice

def LargeField(gameState):
    print("You are in the large field.")
    print("What would you like to do?")
    choice = getChoice(["Go to Water front (1)","Go to Forest (2)", "Go to Spider Field (4)","Go to Dunes (5)","Save Game"])
    match choice:
        case "Go to Water front (1)":
            gameState.currentLocationID = 1
        case "Go to Forest (2)":
            gameState.currentLocationID = 2
        case "Go to Spider Field (4)":
            gameState.currentLocationID = 4
        case "Go to Dunes (5)":
            gameState.currentLocationID = 5
        case "Save Game":
            gameState.printSaveCode()
            LargeField(gameState)
        case _:
            print("Invalid choice")
            LargeField(gameState)


