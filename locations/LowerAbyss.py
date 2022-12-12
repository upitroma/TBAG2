from GetChoice import getChoice

def LowerAbyss(gameState):
    print("You are at the lower abyss.")
    print("What would you like to do?")
    choice = getChoice(["Go to Pond (3)","Go to Abyss Entrance (9)","Go to Mushroom Area (11)","Save Game"])
    match choice:
        case "Go to Pond (3)":
            gameState.currentLocationID = 3
        case "Go to Abyss Entrance (9)":
            gameState.currentLocationID = 9
        case "Go to Mushroom Area (11)":
            gameState.currentLocationID = 11
        case "Save Game":
            gameState.printSaveCode()
            LowerAbyss(gameState)
        case _:
            print("Invalid choice")
            LowerAbyss(gameState)