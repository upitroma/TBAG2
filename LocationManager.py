from GetChoice import getChoice
from locations.BaseCamp import BaseCamp
from locations.WaterFront import WaterFront
from locations.LargeField import LargeField
from locations.Dunes import Dunes
from locations.Waterfall import Waterfall
from locations.Cliff import Cliff
from locations.Forest import Forest
from locations.Pond import Pond
from locations.SpiderField import SpiderField
from locations.AbyssEntrance import AbyssEntrance
from locations.LowerAbyss import LowerAbyss
from locations.MushroomArea import MushroomArea


areas = ["Base Camp", "Water Front (1)" "Forest (2)", "Pond (3)", "Spider Field (4)", "Dunes (5)", "Large Field (6)", "Waterfall (7)", "Cliff (8)", "Abyss Entrance (9)", "Lower Abyss (10)", "Mushroom Area (11)"]


def loadLevel(gamestate):
    while True:
        print("\033[H\033[J", end="")
        match gamestate.currentLocationID:
            case 0:
                BaseCamp(gamestate)
            case 1:
                WaterFront(gamestate)
            case 2:
                Forest(gamestate)
            case 3:
                Pond(gamestate)
            case 4:
                SpiderField(gamestate)
            case 5:
                Dunes(gamestate)
            case 6:
                LargeField(gamestate)
            case 7:
                Waterfall(gamestate)
            case 8:
                Cliff(gamestate)
            case 9:
                AbyssEntrance(gamestate)
            case 10:
                LowerAbyss(gamestate)
            case 11:
                MushroomArea(gamestate)
            case _:
                print("You are in an unknown area.")
                quit()
    