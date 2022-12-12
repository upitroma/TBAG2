from GetChoice import getChoice

def AbyssEntrance(gameState):
    print("You are at the abyss entrance.")
    print("What would you like to do?")
    choice = getChoice(["Go to Cliff (8)","Go to Lower Abyss (10)","Go to Mushroom Area (11)","Save Game"])
    match choice:
        case "Go to Cliff (8)":
            gameState.currentLocationID = 8
        case "Go to Lower Abyss (10)":
            gameState.currentLocationID = 10
        case "Go to Mushroom Area (11)":
            gameState.currentLocationID = 11
        case "Save Game":
            gameState.printSaveCode()
            AbyssEntrance(gameState)
        case _:
            print("Invalid choice")
            AbyssEntrance(gameState)