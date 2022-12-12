from GetChoice import getChoice

def Waterfall(gamestate):
    print("You are at the waterfall.")
    print("What would you like to do?")
    choice = getChoice(["Go to Pond (3)","Go to Spider Field (4)","Go to Cliff (8)","Save Game"])
    match choice:
        case "Go to Pond (3)":
            gamestate.currentLocationID = 3
        case "Go to Spider Field (4)":
            gamestate.currentLocationID = 4
        case "Go to Cliff (8)":
            gamestate.currentLocationID = 8
        case "Save Game":
            gamestate.printSaveCode()
            Waterfall(gamestate)
        case _:
            print("Invalid choice")
            Waterfall(gamestate)
