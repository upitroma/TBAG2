from GetChoice import getChoice
from locations.BaseCamp import BaseCamp
from locations.WaterFront import WaterFront
from locations.LargeField import LargeField

areas = ["Base Camp", "Water Front (1)" "Forest (2)", "Pond (3)", "Spider Field (4)", "Dunes (5)", "Large Field (6)", "Waterfall (7)", "Cliff (8)", "Abyss Entrance (9)", "Lower Abyss", "Mushroom Area (11)"]


def loadLevel(gamestate):
    while True:
        print("\033[H\033[J", end="")
        match gamestate.currentLocationID:
            case 0:
                BaseCamp(gamestate)
            case 1:
                WaterFront(gamestate)
            case 6:
                LargeField(gamestate)
            case _:
                print("You are in an unknown area.")
                quit()
    