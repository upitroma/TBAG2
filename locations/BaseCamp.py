from GetChoice import getChoice

def BaseCamp(gameState):
    print("You are in the base camp.")
    print("What would you like to do?")
    choice = getChoice(["check item box","Go to Water Front (1)","Save Game"])
    match choice:
        case "check item box":
            print("You have the following items:")
            BaseCamp(gameState)
        case "Go to Water Front (1)":
            gameState.currentLocationID = 1
        case "Save Game":
            gameState.printSaveCode()
            BaseCamp(gameState)
        case _:
            print("Invalid choice")
            BaseCamp(gameState)

