from GetChoice import getChoice

def MushroomArea(gamestate):
    print("You are at the mushroom area.")
    print("What would you like to do?")
    choice = getChoice(["Go to Abyss Entrance (9)","Go to Mushroom Area (10)","Save Game"])
    match choice:
        case "Go to Abyss Entrance (9)":
            gamestate.currentLocationID = 9
        case "Go to Mushroom Area (10)":
            gamestate.currentLocationID = 10
        case "Save Game":
            gamestate.printSaveCode()
            MushroomArea(gamestate)
        case _:
            print("Invalid choice")
            MushroomArea(gamestate)