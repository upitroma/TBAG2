from GetChoice import getChoice

def SpiderField(gameState):
    print("You are at the spider field.")
    print("What would you like to do?")
    choice = getChoice(["Go to Forest (2)","Go to Dunes (5)","Go to Field (6)","Go to Waterfall (7)","Save Game"])
    match choice:
        case "Go to Forest (2)":
            gameState.currentLocationID = 2
        case "Go to Dunes (5)":
            gameState.currentLocationID = 5
        case "Go to Field (6)":
            gameState.currentLocationID = 6
        case "Go to Waterfall (7)":
            gameState.currentLocationID = 7
        case "Save Game":
            gameState.printSaveCode()
            SpiderField(gameState)
        case _:
            print("Invalid choice")
            SpiderField(gameState)